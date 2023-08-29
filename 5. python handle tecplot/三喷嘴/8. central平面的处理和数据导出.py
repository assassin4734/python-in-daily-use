import tecplot as tp
import os
from tecplot.exception import *
from tecplot.constant import *


tp.session.connect()


def func_central(dir_post_sw_f, yd_f, func_s):
    for num2 in range(len(scale_factor)):
        str_factors = str(scale_factor[num2])
        # 后处理地址
        dir_post_working = dir_post_sw_f + '\\' + \
            str_factors + '\\central-streamline.lay'
        # dir_line = dir_post_sw_f + '\\' + \
        #     str_factors + '\\interline.dat'
        # command_t = "XSTART = 0 YSTART = " + yd_f + " ZSTART = 0 XEND = 2.4 YEND = " + \
        #     yd_f + " ZEND = 0 NUMPTS = 200 EXTRACTTHROUGHVOLUME = F EXTRACTTOFILE = F "
        dir_save = dir_post_working.replace('.lay', '.png')
        # tecplot修改和导出
        tp.load_layout(dir_post_working)
        # tp.macro.execute_command('$!RedrawAll')
        # tp.active_frame().plot().contour(0).colormap_filter.continuous_min = -0.7
        # tp.active_frame().plot().contour(0).colormap_filter.continuous_max = 2
        # tp.macro.execute_command('$!RedrawAll')
        # tp.active_frame().plot().show_shade = True
        # tp.macro.execute_command('$!RedrawAll')
        # tp.active_frame().plot().streamtraces.add(seed_point=[2.45828, 2.70363],
        #                                           stream_type=Streamtrace.TwoDLine)
        # tp.active_frame().plot().streamtraces.add(seed_point=[2.45781, 2.40794],
        #                                           stream_type=Streamtrace.TwoDLine)
        # tp.active_frame().plot().streamtraces.add(seed_point=[2.45734, 2.11225],
        #                                           stream_type=Streamtrace.TwoDLine)
        # tp.active_frame().plot().streamtraces.add(seed_point=[2.45686, 1.81656],
        #                                           stream_type=Streamtrace.TwoDLine)
        # tp.active_frame().plot().streamtraces.add(seed_point=[2.45639, 1.52087],
        #                                           stream_type=Streamtrace.TwoDLine)
        # tp.active_frame().plot().streamtraces.add(seed_point=[2.45592, 1.22518],
        #                                           stream_type=Streamtrace.TwoDLine)
        # tp.active_frame().plot().streamtraces.add(seed_point=[2.45545, 0.929487],
        #                                           stream_type=Streamtrace.TwoDLine)
        # tp.active_frame().plot().streamtraces.add(seed_point=[2.45497, 0.633796],
        #                                           stream_type=Streamtrace.TwoDLine)
        # tp.active_frame().plot().streamtraces.add(seed_point=[2.4545, 0.338105],
        #                                           stream_type=Streamtrace.TwoDLine)
        # tp.active_frame().plot().streamtraces.add(seed_point=[2.45403, 0.0424138],
        #                                           stream_type=Streamtrace.TwoDLine)
        # tp.active_frame().plot().streamtraces.add(seed_point=[0.175415, 1.25399],
        #                                           stream_type=Streamtrace.TwoDLine)
        # tp.active_frame().plot().streamtraces.add(seed_point=[0.175415, 1.1855],
        #                                           stream_type=Streamtrace.TwoDLine)
        # tp.active_frame().plot().streamtraces.add(seed_point=[0.175415, 1.11701],
        #                                           stream_type=Streamtrace.TwoDLine)
        # tp.active_frame().plot().streamtraces.add(seed_point=[0.175415, 1.04852],
        #                                           stream_type=Streamtrace.TwoDLine)
        # tp.active_frame().plot().streamtraces.add(seed_point=[0.175415, 0.980028],
        #                                           stream_type=Streamtrace.TwoDLine)
        # tp.active_frame().plot().streamtraces.add(seed_point=[0.175415, 0.911537],
        #                                           stream_type=Streamtrace.TwoDLine)
        # tp.active_frame().plot().streamtraces.add(seed_point=[0.175415, 0.843047],
        #                                           stream_type=Streamtrace.TwoDLine)
        # tp.active_frame().plot().streamtraces.add(seed_point=[0.175415, 0.774556],
        #                                           stream_type=Streamtrace.TwoDLine)
        # tp.active_frame().plot().streamtraces.add(seed_point=[0.175415, 0.706065],
        #                                           stream_type=Streamtrace.TwoDLine)
        # tp.active_frame().plot().streamtraces.add(seed_point=[0.175415, 0.637574],
        #                                           stream_type=Streamtrace.TwoDLine)
        # tp.macro.execute_extended_command(command_processor_id='Extract Precise Line',
        #                                   command=command_t)
        # tp.data.save_tecplot_ascii(dir_line,
        #                            zones=[1],
        #                            include_text=False,
        #                            precision=9,
        #                            include_geom=False,
        #                            include_data_share_linkage=True,
        #                            use_point_format=True)
        # tp.active_frame().plot().show_shade = False
        # 改坐标轴和向量
        # frame = tp.active_frame()
        # plot = frame.plot(PlotType.Cartesian2D)
        # plot.axes.x_axis.variable_index=28
        # plot.axes.y_axis.variable_index=27
        # tp.macro.execute_command('$!RedrawAll')
        # plot.vector.u_variable_index=30
        # plot.vector.v_variable_index=29
        # tp.macro.execute_command('$!RedrawAll')
        # plot.axes.x_axis.tick_labels.show=False
        # tp.macro.execute_command('$!RedrawAll')
        # plot.axes.y_axis.tick_labels.show=False
        # tp.macro.execute_command('$!RedrawAll')
        # frame.width = 2.15*0.3937
        # plot.axes.x_axis.min = 0
        # plot.axes.x_axis.max = 1
        # func_s()
        tp.export.save_tiff(dir_save,
                            width=3840,
                            region=ExportRegion.AllFrames,
                            supersample=1,
                            convert_to_256_colors=False,
                            gray_scale_depth=None,
                            byte_order=TIFFByteOrder.Intel)
        tp.active_frame().plot().axes.x_axis.line.line_thickness=0.8
        tp.active_frame().plot().axes.y_axis.line.line_thickness=0.8
        tp.active_frame().plot().axes.grid_area.border_thickness=0.8
        print(dir_post_working + ' photo exported')
        tp.save_layout(dir_post_working)
        # tp.save_layout(dir_post_working, use_relative_paths=True)


def func_stream():
    tp.active_frame().plot().show_shade=True
    tp.active_frame().plot().streamtraces.add(seed_point=[0.682116, 0.154122],
        stream_type=Streamtrace.TwoDLine)
    tp.active_frame().plot().streamtraces.add(seed_point=[0.810605, 0.13128],
        stream_type=Streamtrace.TwoDLine)
    tp.active_frame().plot().streamtraces.add(seed_point=[0.899121, 0.162688],
        stream_type=Streamtrace.TwoDLine)
    tp.active_frame().plot().streamtraces.add(seed_point=[0.941951, 0.145556],
        stream_type=Streamtrace.TwoDLine)
    tp.active_frame().plot().streamtraces.add(seed_point=[0.853435, 0.13699],
        stream_type=Streamtrace.TwoDLine)
    tp.active_frame().plot().streamtraces.add(seed_point=[0.973359, 0.105582],
        stream_type=Streamtrace.TwoDLine)
    tp.active_frame().plot().streamtraces.add(seed_point=[0.653562, 0.145556],
        stream_type=Streamtrace.TwoDLine)
    tp.active_frame().plot().streamtraces.add(seed_point=[0.839159, 0.148412],
        stream_type=Streamtrace.TwoDLine)
    tp.active_frame().plot().streamtraces.add(seed_point=[0.950517, 0.413957],
        stream_type=Streamtrace.TwoDLine)
    tp.active_frame().plot().streamtraces.add(seed_point=[0.890555, 0.428234],
        stream_type=Streamtrace.TwoDLine)
    tp.active_frame().plot().streamtraces.add(seed_point=[0.667839, 0.342574],
        stream_type=Streamtrace.TwoDLine)
    tp.active_frame().plot().streamtraces.add(seed_point=[0.5936, 0.334008],
        stream_type=Streamtrace.TwoDLine)
    tp.active_frame().plot().streamtraces.add(seed_point=[0.610732, 0.22265],
        stream_type=Streamtrace.TwoDLine)
    tp.active_frame().plot().streamtraces.add(seed_point=[0.585034, 0.0598963],
        stream_type=Streamtrace.TwoDLine)
    tp.active_frame().plot().streamtraces.add(seed_point=[0.599311, 0.0913049],
        stream_type=Streamtrace.TwoDLine)
    tp.active_frame().plot().streamtraces.add(seed_point=[0.947661, 0.285467],
        stream_type=Streamtrace.TwoDLine)
    tp.active_frame().plot().streamtraces.add(seed_point=[0.0767858, 0.194097],
        stream_type=Streamtrace.TwoDLine)
    tp.active_frame().plot().streamtraces.add(seed_point=[0.0567985, 0.102726],
        stream_type=Streamtrace.TwoDLine)
    tp.active_frame().plot().streamtraces.add(seed_point=[0.0225346, 0.0456197],
        stream_type=Streamtrace.TwoDLine)
    tp.active_frame().plot().show_shade=False



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
            func_central(dir_post_sw, yd, func_stream)
        else:
            swfolder = ['388', '438', '508']
            for sw in swfolder:
                dir_post_sw = dir_post_d + '\\' + sw
                func_central(dir_post_sw, yd, func_stream)
print('all done')
