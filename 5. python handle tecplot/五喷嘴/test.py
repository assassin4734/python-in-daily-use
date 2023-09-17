from tecplot.exception import *
from tecplot.constant import *
import tecplot as tp


tp.session.connect()


tp.macro.execute_extended_command(command_processor_id='Extract Precise Line',
    command='XSTART = -4 YSTART = 0.25 ZSTART = 0 XEND = 4 YEND = 0.25 ZEND = 0 NUMPTS = 400 EXTRACTTHROUGHVOLUME = F EXTRACTTOFILE = F ')
tp.macro.execute_extended_command(command_processor_id='Extract Precise Line',
    command='XSTART = -4 YSTART = 0.5 ZSTART = 0 XEND = 4 YEND = 0.5 ZEND = 0 NUMPTS = 400 EXTRACTTHROUGHVOLUME = F EXTRACTTOFILE = F ')
tp.macro.execute_extended_command(command_processor_id='Extract Precise Line',
    command='XSTART = -4 YSTART = 0.75 ZSTART = 0 XEND = 4 YEND = 0.75 ZEND = 0 NUMPTS = 400 EXTRACTTHROUGHVOLUME = F EXTRACTTOFILE = F ')
tp.macro.execute_extended_command(command_processor_id='Extract Precise Line',
    command='XSTART = -4 YSTART = 1 ZSTART = 0 XEND = 4 YEND = 1 ZEND = 0 NUMPTS = 400 EXTRACTTHROUGHVOLUME = F EXTRACTTOFILE = F ')
# End Macro.

