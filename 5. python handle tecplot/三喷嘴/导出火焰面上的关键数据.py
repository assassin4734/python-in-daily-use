import os
import pandas as pd
import shutil
import tecplot as tp
from tecplot.constant import *
tp.session.connect(port=7600)
'''
0. 先把变量无量纲化定义好；
1. 基于热态数据，插值到矩形网格，再做对应dat的layout；
2. 基于对应dat的layout里面的热态数据，提取等值线c=0.7；
3. 提取等值线数据中的坐标值，坐标值是无量纲化的xy坐标，x是V29，y是V28；
4. 把flame的layout复制到冷态场中,然后也要导出dat，才能保证坐标系的一致性；
5. 取点读取数据；
6. 用write data as text file导出polyline上的湍流火焰传播速度和速度强度数据；
'''


def tecexport(dir_lay_f, dir_dst_f, dofy):
    tp.load_layout(dir_lay_f)
    tp.macro.execute_command('$!RedrawAll')
    command_t = '''$!CreateRectangularZone 
                IMax = 200
                JMax = 200
                KMax = 1
                X1 = 0
                Y1 = 0.1
                Z1 = 0
                X2 = ''' + dofy + '''
                Y2 = 2
                Z2 = 0
                XVar = 28
                YVar = 29'''
    tp.macro.execute_command(command_t)
    tp.macro.execute_command('''$!Pick SetMouseMode
                                MouseMode = Select''')
    tp.active_frame().plot().show_mesh = True
    tp.macro.execute_command('$!RedrawAll')
    tp.data.operate.interpolate_linear(source_zones=[0],
                                       destination_zone=1,
                                       variables=range(0, 31))
    tp.macro.execute_command('$!RedrawAll')
    tp.data.save_tecplot_ascii(dir_dst_f,
                               zones=[1],
                               variables=range(0, 31),
                               include_text=False,
                               precision=9,
                               include_geom=False,
                               include_data_share_linkage=True,
                               use_point_format=True)
    tp.macro.execute_command('$!RedrawAll')
    print(dir_dst_f + ' 已导出完成')


def copyFile(src, dest):
    try:
        shutil.copy(src, dest)
    # eg. src and dest are the same file
    except shutil.Error as e:
        print('Error: %s' % e)
    # eg. source or destination doesn't exist
    except IOError as e:
        print('Error: %s' % e.strerror)


def rename_data(dir_lay_f):
    txtname = dir_lay_f.replace('.lay', '.txt')
    os.rename(dir_lay_f, txtname)
    # 替换源文件
    file_data = ""
    layout = open(txtname, mode='r', encoding="utf-8")
    for line in layout:
        line = line.replace('central-1.plt', 'flame.dat')
        file_data += line
    newlayout = open(txtname.replace('.txt', 'dat.txt'),
                     mode='w', encoding="utf-8")
    newlayout.write(file_data)
    layout.close()
    newlayout.close()
    newlayname = txtname.replace('.txt', 'dat.lay')
    try:
        os.rename(txtname.replace('.txt', 'dat.txt'), newlayname)
    except:
        os.remove(newlayname)
        os.rename(txtname.replace('.txt', 'dat.txt'), newlayname)
    os.rename(txtname, dir_lay_f)
    print("# 修改源文件已完成")
    return(newlayname)


def extractcounterline(dir_new,loc):
    tp.load_layout(dir_new)
    tp.macro.execute_command('$!RedrawAll')
    tp.macro.execute_command('''$!CreateContourLineZones 
                                ContLineCreateMode = OneZonePerContourLevel''')
    csvfile = loc + '\\counterline.csv'
    commandcon = 'VarNames:FrOp=1:ZnCount=1:ZnList=[2]:AllVars:ValSep=",":FNAME="' + loc + '\\counterline.csv' + '"'
    tp.macro.execute_extended_command(command_processor_id='excsv',
                                      command=commandcon)
    tp.macro.execute_command('$!RedrawAll')
    return(csvfile)


def hotflowfield(sw):
    # 提取等值线
    dir_hot_scale = dir_hot_d + '\\' + sw + '\\' + str(scale)
    dir_hot_lay = dir_hot_scale + '\\flame.lay'
    dir_hot_dat = dir_hot_scale + '\\flame.dat'
    tecexport(dir_hot_lay, dir_hot_dat, y_d)
    newlay_hot = dir_hot_lay.replace('flame.lay', 'flamedat.lay')
    rename_data(dir_hot_lay)
    dir_csv = extractcounterline(newlay_hot, dir_hot_scale)
    # 提取坐标值
    row = pd.read_csv(dir_csv, sep=',')
    print(row)
    xcor = list(row["V29"])
    ycor = list(row["V28"])
    hotpoints = [(x, y) for x, y in zip(xcor, ycor)]
    print(hotpoints)
    return(dir_hot_lay, hotpoints)


def coldflowfield(dir_hot_tem, points, sw):
    # 定义出湍流火焰传播速度和速度的列表
    t_f_s = []
    m_v = []
    # 对冷态场文件进行处理
    dir_cold_scale = dir_cold_d + '\\' + sw + '\\' + str(scale)
    dir_cold_lay = dir_cold_scale + '\\flame.lay'
    dir_cold_dat = dir_cold_scale + '\\flame.dat'
    copyFile(dir_hot_tem, dir_cold_lay)
    tecexport(dir_cold_lay, dir_cold_dat, y_d)
    newlay_cold = rename_data(dir_cold_lay)
    # 取点操作
    tp.load_layout(newlay_cold)
    tp.active_frame().plot().show_shade=True
    tp.active_frame().plot().fieldmaps(0).shade.color=Color.Custom2
    # 用polyline难以捋顺点的方向
    # frame = tp.active_frame()
    # line = frame.add_polyline(points, coord_sys=CoordSys.Grid)
    # line.position = (0,0)
    # line.line_thickness = 0.5
    # line.color = Color.Blue
    # 取点
    for point in points:
        px = point[0]
        py = point[1]
        result = tp.data.query.probe_at_position(px, py)
        if result is None:
            pass
        else:
            data = result[0]
            print(data)
            t_f_s.append(data[5])
            m_v.append(data[24])
    return t_f_s, m_v, dir_cold_scale


def savedata(tfs, mv, loc):
    # 把两个列表拼成dataframe
    df = pd.DataFrame({'turbulent flame speed':tfs, 'velocity magnitude':mv})
    print(df)
    df.to_excel(loc+'\\data.xlsx', index=False)
    print("数据已经保存")



if __name__ == "__main__":
    # 定义计算根目录
    dir_hot = "E:\\0-PhD\\3 nozzle\\postprocessing\\"
    dir_cold = "E:\\0-PhD\\3 nozzle\\coldflowfield\\postprocessing\\"
    # 定义目录变量
    distance_folder = ['1925', '1625', '2250']
    scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
    #
    print('# 找到工作目录')
    #
    for scale in scale_factor:
        for di in range(len(distance_folder)):
            # G:\\assassin\\3nozzle\\1625
            distance = distance_folder[di]
            # 定义导出网格区域的高度
            y_d = str(int(distance)*0.001*0.5)
            # 定义新目录
            dir_hot_d = dir_hot + distance
            dir_cold_d = dir_cold + distance
            # 变间距目录
            # G:\\assassin\\3nozzle\\1625\\388
            if distance != '1925':
                sw = '438'
                hot_tem, hot_points = hotflowfield(sw)
                data_tfs, data_mv, saveloc = coldflowfield(hot_tem, hot_points, sw)
                savedata(data_tfs, data_mv, saveloc)
            else:
                swfolder = ['388', '438', '508']
                for sw in swfolder:
                    hot_tem, hot_points = hotflowfield(sw)
                    data_tfs, data_mv, saveloc = coldflowfield(hot_tem, hot_points, sw)
                    savedata(data_tfs, data_mv, saveloc)
print('all done')
