import tecplot as tp
import os
from tecplot.exception import *
from tecplot.constant import *


tp.session.connect()


def func_central(dir_post_sw_f, yd_f):
    for num2 in range(len(scale_factor)):
        str_factors = str(scale_factor[num2])
        # 后处理地址
        dir_post_working = dir_post_sw_f + '\\' + \
            str_factors + '\\central-streamline.lay'
        dir_line = dir_post_sw_f + '\\' + \
            str_factors + '\\interline.dat'
        command_t = "XSTART = 0 YSTART = " + yd_f + " ZSTART = 0 XEND = 2.4 YEND = " + yd_f + " ZEND = 0 NUMPTS = 200 EXTRACTTHROUGHVOLUME = F EXTRACTTOFILE = T EXTRACTFILENAME = '" + dir_line + "' "
        dir_save = dir_post_working.replace('.lay', '.png')
        # tecplot修改和导出
        tp.load_layout(dir_post_working)
        tp.macro.execute_command('$!RedrawAll')
        tp.active_frame().plot().contour(0).colormap_filter.continuous_min = -0.7
        tp.active_frame().plot().contour(0).colormap_filter.continuous_max = 2
        tp.macro.execute_command('$!RedrawAll')
        tp.macro.execute_command('$!RedrawAll')
        tp.active_frame().plot().show_shade = True
        tp.macro.execute_command('$!RedrawAll')
        tp.active_frame().plot().streamtraces.add(seed_point=[2.45828, 2.70363],
                                                  stream_type=Streamtrace.TwoDLine)
        tp.active_frame().plot().streamtraces.add(seed_point=[2.45781, 2.40794],
                                                  stream_type=Streamtrace.TwoDLine)
        tp.active_frame().plot().streamtraces.add(seed_point=[2.45734, 2.11225],
                                                  stream_type=Streamtrace.TwoDLine)
        tp.active_frame().plot().streamtraces.add(seed_point=[2.45686, 1.81656],
                                                  stream_type=Streamtrace.TwoDLine)
        tp.active_frame().plot().streamtraces.add(seed_point=[2.45639, 1.52087],
                                                  stream_type=Streamtrace.TwoDLine)
        tp.active_frame().plot().streamtraces.add(seed_point=[2.45592, 1.22518],
                                                  stream_type=Streamtrace.TwoDLine)
        tp.active_frame().plot().streamtraces.add(seed_point=[2.45545, 0.929487],
                                                  stream_type=Streamtrace.TwoDLine)
        tp.active_frame().plot().streamtraces.add(seed_point=[2.45497, 0.633796],
                                                  stream_type=Streamtrace.TwoDLine)
        tp.active_frame().plot().streamtraces.add(seed_point=[2.4545, 0.338105],
                                                  stream_type=Streamtrace.TwoDLine)
        tp.active_frame().plot().streamtraces.add(seed_point=[2.45403, 0.0424138],
                                                  stream_type=Streamtrace.TwoDLine)
        tp.active_frame().plot().streamtraces.add(seed_point=[0.175415, 1.25399],
                                                  stream_type=Streamtrace.TwoDLine)
        tp.active_frame().plot().streamtraces.add(seed_point=[0.175415, 1.1855],
                                                  stream_type=Streamtrace.TwoDLine)
        tp.active_frame().plot().streamtraces.add(seed_point=[0.175415, 1.11701],
                                                  stream_type=Streamtrace.TwoDLine)
        tp.active_frame().plot().streamtraces.add(seed_point=[0.175415, 1.04852],
                                                  stream_type=Streamtrace.TwoDLine)
        tp.active_frame().plot().streamtraces.add(seed_point=[0.175415, 0.980028],
                                                  stream_type=Streamtrace.TwoDLine)
        tp.active_frame().plot().streamtraces.add(seed_point=[0.175415, 0.911537],
                                                  stream_type=Streamtrace.TwoDLine)
        tp.active_frame().plot().streamtraces.add(seed_point=[0.175415, 0.843047],
                                                  stream_type=Streamtrace.TwoDLine)
        tp.active_frame().plot().streamtraces.add(seed_point=[0.175415, 0.774556],
                                                  stream_type=Streamtrace.TwoDLine)
        tp.active_frame().plot().streamtraces.add(seed_point=[0.175415, 0.706065],
                                                  stream_type=Streamtrace.TwoDLine)
        tp.active_frame().plot().streamtraces.add(seed_point=[0.175415, 0.637574],
                                                  stream_type=Streamtrace.TwoDLine)
        tp.macro.execute_extended_command(command_processor_id='Extract Precise Line',
                                          command=command_t)
        tp.active_frame().plot().show_shade = False
        tp.macro.execute_command('$!RedrawAll')
        frame = tp.active_frame()
        plot = frame.plot(PlotType.Cartesian2D)
        plot.axes.x_axis.ticks.auto_spacing = False
        plot.axes.x_axis.ticks.spacing = 1
        tp.export.save_tiff(dir_save,
                           width=7680,
                           region=ExportRegion.AllFrames,
                           supersample=1,
                           convert_to_256_colors=False,
                           gray_scale_depth=None,
                           byte_order=TIFFByteOrder.Intel)
        print(dir_post_working + ' photo exported')
        tp.save_layout(dir_post_working, use_relative_paths=True)


if __name__ == "__main__":
    # 定义计算根目录
    dir_post = "E:\\0-PhD\\3 nozzle\\postprocessing\\"
    # 定义目录变量
    distance_folder = ['1625', '1925', '2250']
    yd_folder = ['0.8125', '0.9625', '1.125']
    scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
    #
    print('# 找到工作目录')
    #
    for num1 in range(len(distance_folder)):
        # G:\\assassin\\3nozzle\\1625
        distance = distance_folder[num1]
        dir_post_d = dir_post + distance
        yd = yd_folder[num1]
        # 变间距目录
        # G:\\assassin\\3nozzle\\1625\\388
        if distance != '1925':
            sw = '438'
            dir_post_sw = dir_post_d + '\\' + sw
            func_central(dir_post_sw, yd)
        else:
            swfolder = ['388', '438', '508']
            for sw in swfolder:
                dir_post_sw = dir_post_d + '\\' + sw
                func_central(dir_post_sw, yd)
print('all done')
