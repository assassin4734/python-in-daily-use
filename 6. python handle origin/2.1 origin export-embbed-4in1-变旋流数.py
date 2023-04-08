import originpro as op


# 定义文件目录
file_folder = [28.5, 35.5, 40.5, 45.5, 52.5]
positions = [1, 2, 3, 4]
data_val = input('请输入想要导出的变量名称')
# 定义统计物理量的目录以及建立统计表
for folders in file_folder:
    str_folders = str(folders)
    dir_colletion = 'E:\\0-PhD\\1 nozzle\\different swirl number\\postprocessing\\z-' + str_folders
    print(dir_colletion + ' is on processing')
    src_opju = dir_colletion + '\\' + data_val + '.opju'
    print(src_opju)
    op.open(file = src_opju, readonly = False)
    graphs = 1
    while graphs < 5:
        position = str(positions[graphs - 1])
        gp = op.find_graph('Graph' + str(graphs))
        if data_val == '无量纲轴向速度':
            gp[0].yscale = 1   
            gp[0].set_ylim(begin=-1.5, end=2, step=0.5)
        elif data_val == '无量纲径向速度':
            gp[0].yscale = 1   
            gp[0].set_ylim(begin=-0.5, end=2, step=0.5)
        else:
            pass
        gp[0].xscale = 1   
        gp[0].set_xlim(begin=0, end=1.5, step=0.5)
        exp_file = dir_colletion + '\\z-' + str(folders) + '-' + data_val + '-' + position + '.png'
        gp.save_fig(path=exp_file, width=1500)
        print(f'Graph exported: {exp_file}')
        graphs += 1
    op.save(src_opju)
op.exit()
input("全部完成，输入回车关闭程序")