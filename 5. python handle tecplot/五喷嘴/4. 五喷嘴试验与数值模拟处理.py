import tecplot as tp
from tecplot.exception import *
from tecplot.constant import *
import os, re


tp.session.connect(port=7600)


dir = "E:\\0-PhD\\5 nozzle\\5 nozzle piv experiments and numerical simulation\\"
category = ["experiments", "simulation"]
nozzles = ["5nozzle open", "3nozzle open", "1nozzle open"]
for cate in category:
    dir_cate = dir + cate + "\\"
    for nozzle in nozzles:
        dir_nozzle = dir_cate + nozzle + "\\"
        layouts = []
        files = os.listdir(dir_nozzle)
        for file in files:
            if re.search(".lay", file, re.I):
                layouts.append(file)
        for lay in layouts:
            print(lay)
        for lay in layouts:
            photo_name = lay.replace('.lay','.tiff')
            dir_photosave = dir_nozzle + photo_name
            tp.load_layout(dir_nozzle + lay)
            frame = tp.active_frame()
            print(frame)
            plot = frame.plot(PlotType.Cartesian2D)
            xaxis = plot.axes.x_axis
            xaxis.min = 0
            xaxis.max = 2.5
            frame.height = 11.1/2.54
            tp.export.save_tiff(dir_photosave,
                width=1642,
                region=ExportRegion.AllFrames,
                supersample=1,
                convert_to_256_colors=False,
                gray_scale_depth=None,
                byte_order=TIFFByteOrder.Intel)
            print(photo_name + ' photo exported')
            tp.save_layout(dir_nozzle + lay, use_relative_paths=True)
