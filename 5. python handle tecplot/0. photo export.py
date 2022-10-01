import tecplot as tp
from tecplot.exception import *
from tecplot.constant import *




tp.session.connect(port=7600)

file_folder = [28.5, 35.5, 40.5, 45.5, 52.5]
scale_factor = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

for folders in file_folder:
  for factors in scale_factor:

    str_folders = str(folders)
    str_factors = str(factors)
    
    dir_import_velocity = 'F:\\PhD\\1 nozzle\\different swirl number\\postprocessing\\z-' + str_folders + '\\' + str_folders + '-' + str_factors + '\\z-28.5-1-velocity.lay'
    dir_import_flame = 'F:\\PhD\\1 nozzle\\different swirl number\\postprocessing\\z-' + str_folders + '\\' + str_folders + '-' + str_factors + '\\z-28.5-1-flame.lay'
    dir_import_ch = 'F:\\PhD\\1 nozzle\\different swirl number\\postprocessing\\z-' + str_folders + '\\' + str_folders + '-' + str_factors + '\\z-28.5-1-ch+.lay'
    dir_export_velocity = 'F:\\PhD\\1 nozzle\\different swirl number\\postprocessing\\z-' + str_folders + '\\' + str_folders + '-' + str_factors + '\\velocity.tiff'
    dir_export_flame = 'F:\\PhD\\1 nozzle\\different swirl number\\postprocessing\\z-' + str_folders + '\\' + str_folders + '-' + str_factors + '\\flame.tiff'
    dir_export_ch = 'F:\\PhD\\1 nozzle\\different swirl number\\postprocessing\\z-' + str_folders + '\\' + str_folders + '-' + str_factors + '\\ch+.tiff'
    
    print(str_folders + str_factors + 'is on going')
    
    tp.macro.execute_command('$!RedrawAll')
    tp.load_layout(dir_import_velocity)
    tp.export.save_tiff(dir_export_velocity,
        width=730,
        region=ExportRegion.AllFrames,
        supersample=1,
        convert_to_256_colors=False,
        gray_scale_depth=None,
        byte_order=TIFFByteOrder.Intel)
    print('velocity photo exported')
    tp.macro.execute_command('$!RedrawAll')
    tp.load_layout(dir_import_flame)
    tp.export.save_tiff(dir_export_flame,
        width=730,
        region=ExportRegion.AllFrames,
        supersample=1,
        convert_to_256_colors=False,
        gray_scale_depth=None,
        byte_order=TIFFByteOrder.Intel)
    print('flame photo exported')
    tp.macro.execute_command('$!RedrawAll')
    tp.load_layout(dir_import_ch)
    tp.export.save_tiff(dir_export_ch,
        width=730,
        region=ExportRegion.AllFrames,
        supersample=1,
        convert_to_256_colors=False,
        gray_scale_depth=None,
        byte_order=TIFFByteOrder.Intel)
    print('ch photo exported')

input("all done")


