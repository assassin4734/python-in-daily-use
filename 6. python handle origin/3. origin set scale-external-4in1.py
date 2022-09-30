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
# 定义文件目录
file_folder = [28.5, 35.5, 40.5, 45.5, 52.5]
positions = [10, 20, 40, 60]
data_val = input('请输入想要处理的变量名称：')
# 定义统计物理量的目录以及建立统计表
for folders in file_folder:
    str_folders = str(folders)
    dir_colletion = 'F:\\PhD\\1 nozzle\\different swirl number\\postprocessing\\z-' + str_folders
    print(dir_colletion + ' is on processing')
    src_opju = dir_colletion + '\\' + data_val + '.opju'
    print(src_opju)
    ori_project = op.open(file = src_opju, readonly = False)
    graphs = 1
    while graphs < 5:
        position = str(positions[graphs - 1])
        gp = op.find_graph('Graph' + str(graphs))
        exp_file = dir_colletion + '\\z-' + str_folders + '-' + data_val + '-' + position + '.tiff'
        gp[0].yscale = 1   
        gp[0].set_ylim(begin=0, end=0.22, step=0.05)
        graphs += 1
    op.save(src_opju)
op.exit()
input("全部完成，输入回车关闭程序")