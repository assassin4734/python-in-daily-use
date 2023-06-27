import tecplot as tp
from tecplot.exception import *
from tecplot.constant import *

# Uncomment the following line to connect to a running instance of Tecplot 360:
# tp.session.connect()

tp.macro.execute_command('$!RedrawAll')
tp.macro.execute_command('''$!CreateRectangularZone 
  IMax = 200
  JMax = 200
  KMax = 1
  X1 = -0.036
  Y1 = -1.54
  Z1 = 0
  X2 = 5.84
  Y2 = 1.54
  Z2 = 0
  XVar = 29
  YVar = 28''')
tp.macro.execute_command('''$!Pick SetMouseMode
  MouseMode = Select''')
tp.macro.execute_command('$!RedrawAll')
tp.data.operate.interpolate_linear(source_zones=[0],
    destination_zone=1,
    variables=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26])
tp.macro.execute_command('$!RedrawAll')
tp.data.save_tecplot_ascii('E:\\0-PhD\\1 nozzle\\eq\\postprocessing-transport\\eq=0.55\\0.9\\dimensionless oh-cutregion.dat',
    zones=[1],
    variables=[12,27,28],
    include_text=False,
    precision=9,
    include_geom=False,
    include_data_share_linkage=True)
# End Macro.

