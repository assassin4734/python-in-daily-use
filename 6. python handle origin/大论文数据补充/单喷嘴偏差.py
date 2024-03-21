import originpro as op


# 定义文件目录
dir_colletion = 'E:\\0-PhD\\019020210023\\补充分析-单旋流特征'
data_val = ['SW的偏差统计', 'ER的偏差统计']
# 定义统计物理量的目录以及建立统计表
for data in data_val:
    src_opju = dir_colletion + '\\' + data + '.opju'
    print(src_opju)
    op.open(file = src_opju, readonly = False)
    graphs = 0
    var=['回流区长度偏差', '回流区直径偏差', '涡心轴向的偏差', '涡心径向的偏差', '火焰长度的偏差', '火焰张角的偏差']
    while graphs < 6:
        gp = op.find_graph('Graph' + str(graphs+1))
        gp[0].yscale = 1   
        gp[0].set_ylim(begin=0, end=80, step=15)
        exp_file = dir_colletion + '\\' + data + '-' + var[graphs] + '.png'
        gp.save_fig(path=exp_file, width=1500)
        print(f'Graph exported: {exp_file}')
        graphs += 1
    op.save(src_opju)
op.exit()
input("全部完成，输入回车关闭程序")