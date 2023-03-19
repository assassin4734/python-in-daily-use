import originpro as op
import sys


def origin_shutdown_exception_hook(exctype, value, traceback):
    '''Ensures Origin gets shut down if an uncaught exception'''
    op.exit()
    sys.__excepthook__(exctype, value, traceback)

if op and op.oext:
    sys.excepthook = origin_shutdown_exception_hook
if op.oext:
    op.set_show(True)


# 定义目录
distance_folder = ['48', '60', '72']
nozzles_folder = ['5nozzle', '3nozzle', '1nozzle']
quantities = ['无量纲轴向速度.opju', '无量纲径向速度.opju', 'turbulent-flame-speed.opju']
positions = [10, 20, 40, 60]
error_dir = []
for nozzles in nozzles_folder:
    # E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\postprocessing\\5nozzle\\
    dir_nozzles = 'E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\postprocessing\\' + nozzles
    print(dir_nozzles + ' is on processing')
    for distance in distance_folder:
        # E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\5nozzle\\48
        dir_distance = dir_nozzles + '\\' + distance
        for quantity in quantities:
            src_opju = dir_distance + '\\' + quantity
            print(src_opju)
            if quantity == '无量纲轴向速度.opju':
                min = -0.5
                max = 1.25
                ste = 0.5
            elif quantity == '无量纲径向速度.opju':
                min = -0.7
                max = 0.7
                ste = 0.4
            elif quantity == 'turbulent-flame-speed.opju':
                min = 0
                max = 0.09
                ste = 0.025
            op.open(file = src_opju, readonly = False)
            graphs = 1
            while graphs < 5:
                position = str(positions[graphs - 1])
                gp = op.find_graph('Graph' + str(graphs))
                gp[0].yscale = 1   
                gp[0].set_ylim(begin=min, end=max, step=ste)
                graphs += 1
                op.save(src_opju)
op.exit()
input("全部完成，输入回车关闭程序")