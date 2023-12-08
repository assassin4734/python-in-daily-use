import os
import tecplot as tp
from tecplot.exception import *
from tecplot.constant import *


tp.session.connect()


def find_lay(current_file):
    lay_list = []    # 用列表储存txt文件的路径
    for names in current_file:
        if ".lay" in names and "mode" in names:
            lay_list.append(names)
        else:
            pass
    return lay_list


def exportfun(dir_post_working):
    file = find_lay(os.listdir(dir_post_working))
    for lay in file:
        print(dir_post_working+lay + 'is on processing')
        photo_name = lay.replace('.lay', '')
        dir_save = dir_post_working + photo_name + '.png'
        try:
            tp.load_layout(dir_post_working+lay)
            tp.export.save_tiff(dir_save,
                                width=3840,
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
    '''
    程序主体
    '''
    print('定位后处理的目录')
    nozzle_folder = ['5nozzle', '3nozzle', '1nozzle']
    scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
    dir = 'E:\\0-PhD\\5 nozzle\\0-5NOZZLE-DLN2.6SIZE\\postprocessing\\'
    for num1 in range(len(nozzle_folder)):
        # G:\\assassin\\3nozzle\\1625
        nozzle = nozzle_folder[num1]
        dir_post_n = dir + nozzle + '\\48\\48-'
        # 定义POD结果保存位置
        dir_pod_matrix = dir + nozzle + '\\pod_results-ch2o\\'
        planes = ['plane1', 'plane2', 'plane3']
        for plane in planes:
            dir_plane = dir_pod_matrix + plane + '\\'
            exportfun(dir_plane)