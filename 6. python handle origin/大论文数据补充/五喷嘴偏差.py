import originpro as op
import os


# 定义文件目录
dir_colletion = 'E:\\0-PhD\\019020210023\\add_quintuple'
data_val = ['MF diversity', 'MS diversity','MP diversity']
# 定义统计物理量的目录以及建立统计表
for data in data_val:
    opjus = []
    src_opju = dir_colletion + '\\' + data + '\\'
    print(src_opju)
    files = os.listdir(src_opju)
    for file in files:    
        if 'opju' in file:
            op.open(file = src_opju+file, readonly = False)
            gp = op.find_graph('Graph1')
            exp_file = src_opju+file.replace('opju', 'png')
            gp.save_fig(path=exp_file, width=1500)
            print(f'Graph exported: {exp_file}')
op.exit()
input("全部完成，输入回车关闭程序")