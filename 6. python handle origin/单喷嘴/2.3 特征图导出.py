import originpro as op


# 定义文件目录
file_folder = ["回流区长度", "回流区直径", "火焰张角", "火焰长度", "涡心径向位置","涡心轴向位置"]
dirlist = ['E:\\0-PhD\\1 nozzle\\eq\\postprocessing-transport\\', 'E:\\0-PhD\\1 nozzle\\different swirl number\\postprocessing\\']
# 定义统计物理量的目录以及建立统计表
for dir in dirlist:
    for folders in file_folder:
        src_opju = dir + folders + '.opju'
        print(src_opju + ' is on processing')
        op.open(file = src_opju, readonly = False)
        gp = op.find_graph('Graph1')
        exp_file = src_opju.strip('.opju') + '.png'
        gp.save_fig(path=exp_file, type='png', width=1500)
        print(f'Graph exported: {exp_file}')
        op.save(src_opju)
    op.exit()
input("全部完成，输入回车关闭程序")