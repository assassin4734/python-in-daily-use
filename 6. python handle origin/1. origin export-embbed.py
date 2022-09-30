import originpro as op




# 定义文件目录
file_folder = [28.5, 35.5, 40.5, 45.5, 52.5]
postion_folder = [10, 20, 40, 60]
data_val = input('请输入想要导出的变量名称')
# 定义统计物理量的目录以及建立统计表
for folders in file_folder:
    str_folders = str(folders)
    dir_colletion = 'F:\\PhD\\1 nozzle\\different swirl number\\postprocessing\\z-' + str_folders
    print(dir_colletion + ' is on processing')
    for positions in postion_folder:
        str_positions = str(positions)
        src_opju = dir_colletion + '\\' + data_val + '-' + str_positions + '.opju'
        print(src_opju)
        op.open(file = src_opju, readonly = True)
        gp = op.find_graph('Graph1')
        exp_file = dir_colletion + '\\z-' + str_folders + '-' + data_val + '-' + str_positions + '.tiff'
        gp.save_fig(exp_file)
        print(f'Graph exported: {exp_file}')
op.exit()
input("全部完成，输入回车关闭程序")