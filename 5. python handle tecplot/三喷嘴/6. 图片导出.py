import os
import re
import tecplot as tp
from tecplot.exception import *
from tecplot.constant import *


tp.session.connect()


def find_lay(current_file):
    lay_list = []    # 用列表储存txt文件的路径
    for names in current_file:
        if re.search(".lay", names, re.I) and (names == '0.75d-p.lay'):
            lay_list.append(names)
        else:
            pass
    return lay_list


def changedotlines():
    tp.macro.execute_command('''$!AttachGeom 
    GeomType = Circle
    AnchorPos
    {
    X = 0
    }
    Color = Red
    LineThickness = 3
    RawData
    0.5''')
    tp.macro.execute_command('$!RedrawAll')
    if distance == '1625':
        tp.macro.execute_command('''$!AttachGeom 
        AnchorPos
            {
            X = 0.8125
            Y = 0.7961547704878639
            }
        Color = Custom2
        LinePattern = DashDotDot
        LineThickness = 3
        RawData
        1
        2
        0 0 
        0.000735039822757 -1.58811461926''')
        tp.macro.execute_command('''$!AttachGeom 
        GeomType = Circle
        AnchorPos
            {
            X = 1.625
            }
        Color = Custom11
        LinePattern = Dashed
        LineThickness = 3
        RawData
        0.5''')

    elif distance == '1925':
        tp.macro.execute_command('''$!AttachGeom 
        AnchorPos
            {
            X = 0.9625
            Y = 0.7961547704878639
            }
        Color = Custom2
        LinePattern = DashDotDot
        LineThickness = 3
        RawData
        1
        2
        0 0 
        0.000735039822757 -1.58811461926''')
        tp.macro.execute_command('''$!AttachGeom 
        GeomType = Circle
        AnchorPos
            {
            X = 1.925
            }
        Color = Custom11
        LinePattern = Dashed
        LineThickness = 3
        RawData
        0.5''')        
    else:
        tp.macro.execute_command('''$!AttachGeom 
        AnchorPos
            {
            X = 1.125
            Y = 0.7961547704878639
            }
        Color = Custom2
        LinePattern = DashDotDot
        LineThickness = 3
        RawData
        1
        2
        0 0 
        0.000735039822757 -1.58811461926''')
        tp.macro.execute_command('''$!AttachGeom 
        GeomType = Circle
        AnchorPos
            {
            X = 2.25
            }
        Color = Custom11
        LinePattern = Dashed
        LineThickness = 3
        RawData
        0.5''')        
    tp.macro.execute_command('$!RedrawAll')        


def exportfun(dir_post_sw_f):
    # 变缩比目录
    for num2 in range(len(scale_factor)):
        str_factors = str(scale_factor[num2])
        # 后处理目录
        dir_post_working = dir_post_sw_f + '\\' + str_factors + '\\'
        print(dir_post_working)
        file = find_lay(os.listdir(dir_post_working))
        for lay in file:
            print(dir_post_working+lay + 'is on processing')
            photo_name = lay.replace('.lay', '')
            dir_save = dir_post_working + photo_name + '.png'
            try:
                tp.load_layout(dir_post_working+lay)
                tp.active_frame().plot().axes.x_axis.line.line_thickness = 0.8
                tp.active_frame().plot().axes.y_axis.line.line_thickness = 0.8
                tp.active_frame().plot().axes.grid_area.border_thickness = 0.8
                changedotlines()
                tp.export.save_tiff(dir_save,
                                    width=width1,
                                    region=ExportRegion.AllFrames,
                                    supersample=1,
                                    convert_to_256_colors=False,
                                    gray_scale_depth=None,
                                    byte_order=TIFFByteOrder.Intel)
                print(photo_name + ' photo exported')
                tp.save_layout(dir_post_working+lay)
            except:
                pass


if __name__ == "__main__":
    # 定义计算根目录
    dir_post = "E:\\0-PhD\\3 nozzle\\postprocessing\\"
    # 定义目录变量
    distance_folder = ['1625', '1925', '2250']
    scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
    #
    print('# 找到工作目录')
    #
    for num1 in range(len(distance_folder)):
        # G:\\assassin\\3nozzle\\1625
        distance = distance_folder[num1]
        dir_post_d = dir_post + distance
        # 变间距目录
        # G:\\assassin\\3nozzle\\1625\\388
        if distance != '1925':
            sw = '438'
            dir_post_sw = dir_post_d + '\\' + sw
            if distance == '1625':
                width1 = 3840
            elif distance == '2250':
                width1 = 5316
            else:
                pass
            exportfun(dir_post_sw)
        else:
            width1 = 4550
            swfolder = ['388', '438', '508']
            for sw in swfolder:
                dir_post_sw = dir_post_d + '\\' + sw
                exportfun(dir_post_sw)
print('all done')
