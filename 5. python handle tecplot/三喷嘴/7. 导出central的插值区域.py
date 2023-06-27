import tecplot as tp
from tecplot.exception import *
from tecplot.constant import *


def tecexport(dir_lay_f, dir_dst_f):
    tp.macro.execute_command('$!RedrawAll')
    tp.load_layout(dir_lay_f)
    tp.macro.execute_command('$!RedrawAll')
    command_t ='''$!CreateRectangularZone 
                IMax = 200
                JMax = 200
                KMax = 1
                X1 = 0
                Y1 = 0
                Z1 = 0
                X2 = 3
                Y2 = 3
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
                                        variables=range(0,30))
    tp.macro.execute_command('$!RedrawAll')
    tp.data.save_tecplot_ascii(dir_dst_f,
                                zones=[1],
                                variables=range(0,30),
                                include_text=False,
                                precision=9,
                                include_geom=False,
                                include_data_share_linkage=True,
                                use_point_format=True)
    tp.macro.execute_command('$!RedrawAll')



tp.session.connect(port=7600)
if __name__ == "__main__":
    fail = []
    # 定义计算根目录
    dir_post = "E:\\0-PhD\\3 nozzle\\postprocessing\\"
    # 定义目录变量
    distance_folder = ['1625','1925','2250']
    sw_folder = ['388', '438', '508']
    scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
    print('# 找到工作目录')
    for distance in distance_folder:
        # G:\\assassin\\3nozzle\\1625
        dir_post_d = dir_post + distance
        for sw in sw_folder:    # 变间距目录
            # G:\\assassin\\3nozzle\\1625\\388
            dir_post_sw = dir_post_d + '\\' + sw
            # 变缩比目录
            for num in range(len(scale_factor)):
                str_factors = str(scale_factor[num])
                dir_post_working = dir_post_sw + '\\' + str_factors + '\\'  # 后处理目录
                print(dir_post_working)
                dir_dst = dir_post_working + 'central-streamline.lay'
                # 
                print('# 导出插值区域')
                # 
                dir_dat = (dir_dst).replace('lay', 'dat')
                try:
                    tecexport(dir_dst, dir_dat)
                except:
                    print('文件不存在')
                    fail.append(dir_dst)
print('all done')
for f in fail:
    print(f)