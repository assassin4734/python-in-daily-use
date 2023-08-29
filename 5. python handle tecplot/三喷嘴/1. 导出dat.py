import os
import shutil
from tecplot.exception import *
from tecplot.constant import *
import tecplot as tp
'''
把处理好的模板文件复制到各个文件夹下，然后再无量纲化，最后重新导出dat文件
'''


tp.session.connect()


# def find_lay(current_file):
#     lay_list = []    # 用列表储存txt文件的路径
#     for names in current_file:
#         if re.search(".lay", names, re.I):
#             newname = names[:-4]
#             lay_to_txt = dir_post_working + newname + '.txt'
#             os.rename(dir_post_working+names, lay_to_txt)
#             lay_list.append(lay_to_txt)
#         else:
#             pass
#     return lay_list


def change(dir_post_sw_f):
    # 先修改好参数
    for num2 in range(len(scale_factor)):
        str_factors = str(scale_factor[num2])
        size = str(0.096*scale_factor[num2])
        model_velocity = str(velocity[num2])
        # 后处理目录
        dir_post_working = dir_post_sw_f + '\\' + str_factors + '\\regionexport.lay'
        if dir_post_working != exam:
            try:
                os.remove(dir_post_working)
            except:
                pass
        dir_dat = dir_post_sw_f + '\\' + str_factors + '\\0.75d.dat'
        # 复制再改成txt
        copyFile(exam, dir_post_working)
        laytxt = dir_post_working.replace('.lay', '.txt')
        os.rename(dir_post_working, laytxt)
        # 改内容
        file_data = ""
        open_txt = open(laytxt, "r", encoding="utf-8")
        for line in open_txt:
            line = line.replace("0.096", size)
            line = line.replace("28.43562", model_velocity)
            file_data += line
        open_txt.close()
        open_txt = open(laytxt, "w", encoding="utf-8")
        open_txt.write(file_data)
        open_txt.close()
        os.rename(laytxt, dir_post_working)
        # 导出区域
        print(dir_post_working + ' 已拷贝修改完成')
        tecexport(dir_post_working, dir_dat, y_d)


def copyFile(src, dest):
    try:
        shutil.copy(src, dest)
    # eg. src and dest are the same file
    except shutil.Error as e:
        print('Error: %s' % e)
    # eg. source or destination doesn't exist
    except IOError as e:
         print('Error: %s' % e.strerror)


def tecexport(dir_lay_f, dir_dst_f, dofy):
    tp.load_layout(dir_lay_f)
    tp.macro.execute_command('$!RedrawAll')
    command_t ='''$!CreateRectangularZone 
                IMax = 200
                JMax = 200
                KMax = 1
                X1 = 0
                Y1 = 0
                Z1 = 0
                X2 = 2
                Y2 = '''+ dofy + '''
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
                                        variables=range(0,31))
    tp.macro.execute_command('$!RedrawAll')
    tp.data.save_tecplot_ascii(dir_dst_f,
                                zones=[1],
                                variables=range(0,31),
                                include_text=False,
                                precision=9,
                                include_geom=False,
                                include_data_share_linkage=True,
                                use_point_format=True)
    tp.macro.execute_command('$!RedrawAll')
    print(dir_dst_f + ' 已导出完成')


if __name__ == "__main__":
    # 定义计算根目录
    dir_post = "E:\\0-PhD\\3 nozzle\\postprocessing\\"
    # 定义目录变量
    distance_folder = ['1625', '1925', '2250']
    scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
    velocity = [28.43562, 25.59206, 22.7485, 19.90494, 17.0614, 12.79603, 11.37425, 9.952468, 8.530687, 7.108905]
    #
    print('# 找到工作目录')
    #
    for num1 in range(len(distance_folder)):
        # G:\\assassin\\3nozzle\\1625
        distance = distance_folder[num1]
        # 定义间距
        # 把导出的Y轴坐标定义好
        y_d = str(int(distance)*0.001)
        dir_post_d = dir_post + distance
        # 变间距目录
        # G:\\assassin\\3nozzle\\1625\\388
        if distance != '1925':
            sw = '438'
            dir_post_sw = dir_post_d + '\\' + sw
            change(dir_post_sw)
        else:
            swfolder = ['388','438', '508']
            for sw in swfolder:
                dir_post_sw = dir_post_d + '\\' + sw
                change(dir_post_sw)
print('all done')