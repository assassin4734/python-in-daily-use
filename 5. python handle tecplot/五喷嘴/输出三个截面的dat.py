from tecplot.exception import *
from tecplot.constant import *
import tecplot as tp


tp.session.connect()


def tecexport(dir_post_scale):
    dir_1 = dir_post_scale + 'q-1.lay'
    dir_2 = dir_post_scale + 'q-2.lay'
    dir_45 = dir_post_scale + 'y-velocity-45.lay'
    dir_files = [dir_1, dir_2, dir_45]
    for i in range(len(dir_files)):
        lay = dir_files[i]
        dir_dst = dir_post_scale + 'plane' + str(i+1) + '.dat'
        tp.load_layout(lay)
        tp.macro.execute_command('$!RedrawAll')
        if 'y-velocity' not in lay:
            command_t ='''$!CreateRectangularZone 
                        IMax = 200
                        JMax = 200
                        KMax = 1
                        X1 = -4
                        Y1 = 0
                        Z1 = 0
                        X2 = 4
                        Y2 = 4
                        Z2 = 0
                        XVar = 28
                        YVar = 29'''
        else:
            command_t ='''$!CreateRectangularZone 
                        IMax = 200
                        JMax = 200
                        KMax = 1
                        X1 = -3.6
                        Y1 = 0
                        Z1 = 0
                        X2 = 3.6
                        Y2 = 4
                        Z2 = 0
                        XVar = 37
                        YVar = 29'''
        tp.macro.execute_command(command_t)
        tp.macro.execute_command('''$!Pick SetMouseMode
                                    MouseMode = Select''')
        tp.active_frame().plot().show_mesh = True
        tp.macro.execute_command('$!RedrawAll')
        if 'y-velocity' not in lay:
            tp.data.operate.interpolate_linear(source_zones=[0],
                                                destination_zone=1,
                                                variables=range(0,32))
            tp.macro.execute_command('$!RedrawAll')
            tp.data.save_tecplot_ascii(dir_dst,
                                        zones=[1],
                                        variables=range(0,32),
                                        include_text=False,
                                        precision=9,
                                        include_geom=False,
                                        include_data_share_linkage=True,
                                        use_point_format=True)
            tp.macro.execute_command('$!RedrawAll')            
        else:
            tp.data.operate.interpolate_linear(source_zones=[0],
                                                destination_zone=1,
                                                variables=range(0,37))            
            tp.macro.execute_command('$!RedrawAll')
            tp.data.save_tecplot_ascii(dir_dst,
                                        zones=[1],
                                        variables=range(0,37),
                                        include_text=False,
                                        precision=9,
                                        include_geom=False,
                                        include_data_share_linkage=True,
                                        use_point_format=True)
            tp.macro.execute_command('$!RedrawAll')
        print(dir_dst + ' 已导出完成')


if __name__ == "__main__":
    # 定义计算根目录
    dir = "E:\\0-PhD\\5 nozzle\\0-5NOZZLE-DLN2.6SIZE\\"
    dir_post = dir + "postprocessing\\"
    # 定义目录变量
    nozzle_folder = ['1nozzle', '3nozzle', '5nozzle']
    scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
    velocity = [40.98, 36.88, 32.78, 28.68, 24.59, 18.44, 16.39, 14.34, 12.29, 10.24]
    #
    print('# 找到工作目录')
    #
    for num1 in range(len(nozzle_folder)):
        # G:\\assassin\\3nozzle\\1625
        nozzle = nozzle_folder[num1]
        dir_post_n = dir_post + nozzle + '\\48\\48-'
        for num2 in range(len(scale_factor)):
            # 定义缩放因子对的变量和目录
            str_factors = str(scale_factor[num2])
            size = str(0.096*scale_factor[num2])
            model_velocity = str(velocity[num2])
            dir_post_scale = dir_post_n + str_factors + '\\'
            print(dir_post_scale + ' 正在处理')
            tecexport(dir_post_scale)