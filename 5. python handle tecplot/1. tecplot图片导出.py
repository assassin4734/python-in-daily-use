import tecplot as tp
from tecplot.exception import *
from tecplot.constant import *




tp.session.connect(port=7600)

file_folder = [28.5, 35.5, 40.5, 45.5, 52.5]
scale_factor = [0.5, 0.7]
layout_names = ["z-28.5-1-velocity.lay", "z-28.5-1-flame.lay", "z-28.5-1-ch+.lay"]
numbers = 0
for folders in file_folder:
  for factors in scale_factor:

    str_folders = str(folders)
    str_factors = str(factors)
    for layout in layout_names:
        full_name = layout.strip("z-28.5-1-")
        a = full_name.split(".")
        a.pop()
        pic_name = "".join(a)
        dir_import = 'F:\\PhD\\1 nozzle\\re\\postprocessing\\z-' + str_folders + '\\' + str_folders + '-' + str_factors + '\\' + layout
        dir_export = 'F:\\PhD\\1 nozzle\\re\\postprocessing\\z-' + str_folders + '\\' + str_folders + '-' + str_factors + '\\' + pic_name + '.tiff'
        print(str_folders + "-" + str_factors + ' is on going')        
        tp.macro.execute_command('$!RedrawAll')
        tp.load_layout(dir_import)
        tp.export.save_tiff(dir_export,
            width=730,
            region=ExportRegion.AllFrames,
            supersample=1,
            convert_to_256_colors=False,
            gray_scale_depth=None,
            byte_order=TIFFByteOrder.Intel)
        print(pic_name + ' photo exported')
        numbers += 1
numbers = str(numbers)
input("all done, " + numbers + " photos exported")


