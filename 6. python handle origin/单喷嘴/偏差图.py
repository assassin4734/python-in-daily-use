import originpro as op


# 定义文件目录
dir = 'E:\\0-PhD\\1 nozzle\\本章图片\\偏差\\'
names = ['变旋流数.opju', '变当量比.opju']
# 定义统计物理量的目录以及建立统计表
for name in names:
    dir_op = dir + name
    print(dir_op + ' is on processing')
    op.open(file = dir_op, readonly = False)
    graphs = ['6', '7', '8', '9', '10']
    for graph in graphs:
        gp = op.find_graph('Graph' + graph)
        exp_file = dir_op.replace('.opju', '') + '-' + graph + '.png'
        gp.save_fig(path=exp_file, type='png', width=1500)
        print(f'Graph exported: {exp_file}')
    op.save(dir_op)
input("全部完成，输入回车关闭程序")