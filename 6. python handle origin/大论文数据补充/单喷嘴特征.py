import originpro as op
import os


# 定义文件目录
dir_colletion = 'E:\\0-PhD\\019020210023\\add_single'
data_val = ['SW', 'ER']
# 定义统计物理量的目录以及建立统计表
for data in data_val:
    src_opju = dir_colletion + '\\' + data + '\\'
    files = os.listdir(src_opju)
    opjufiles = []
    for file in files:
        if '.opju' in file:
            opjufiles.append(file)
    for opjufile in opjufiles:
        op.open(file = src_opju+opjufile, readonly = False)
        gp = op.find_graph('Graph1')
        exp_file = src_opju + opjufile.replace(data, '') + '.png'
        gp.save_fig(path=exp_file, width=1500)
        print(f'Graph exported: {exp_file}')
    op.save(src_opju)
op.exit()
input("全部完成，输入回车关闭程序")