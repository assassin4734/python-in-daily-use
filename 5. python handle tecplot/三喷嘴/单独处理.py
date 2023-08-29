from tecplot.exception import *
from tecplot.constant import *
import tecplot as tp


tp.session.connect()


tp.load_layout('E:\\0-PhD\\3 nozzle\\postprocessing\\2250\\438\\0.35\\regionexport.lay')
tp.macro.execute_command('$!RedrawAll')
command_t ='''$!CreateRectangularZone 
            IMax = 200
            JMax = 200
            KMax = 1\n  X1 = '''+ '2.25' + '''    \nY1 = 0
            Z1 = 0
            X2 = 0
            Y2 = 0.8
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
tp.data.save_tecplot_ascii('E:\\0-PhD\\3 nozzle\\postprocessing\\2250\\438\\0.35\\1d.dat',
                            zones=[1],
                            variables=range(0,31),
                            include_text=False,
                            precision=9,
                            include_geom=False,
                            include_data_share_linkage=True,
                            use_point_format=True)
tp.macro.execute_command('$!RedrawAll')
