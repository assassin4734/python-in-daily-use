import originpro as op
import os


def originexport(dir_post_sw_f):
    '''
    读取并导出图片
    '''
    files = os.listdir(dir_post_sw_f)
    opjufiles = []
    for file in files:
        if '.opju' in file:
            opjufiles.append(file)
    for opjufile in opjufiles:
        src_opju = dir_post_sw_f + '\\' + opjufile
        op.open(file = src_opju, readonly = False)
        gp = op.find_graph('Graph1')
        exp_file = src_opju.replace('.opju', '.png')
        gp.save_fig(path=exp_file, type='png', width=1500)
        print(f'Graph exported: {exp_file}')
    op.save(src_opju)


if __name__ == "__main__":
    # 定义计算根目录
    dir_post = "E:\\0-PhD\\3 nozzle\\postprocessing\\"
    # 定义目录变量
    distance_folder = ['1625', '1925', '2250']
    yd_folder = ['0.8125', '0.9625', '1.125']
    scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
    #
    print('# 找到工作目录')
    #
    for num1 in range(len(distance_folder)):
        # G:\\assassin\\3nozzle\\1625
        distance = distance_folder[num1]
        dir_post_d = dir_post + distance
        # 变间距目录
        # G:\\assassin\\3nozzle\\1625\\388
        if distance != '1925':
            sw = '438'
            dir_post_sw = dir_post_d + '\\' + sw
            originexport(dir_post_sw)
        else:
            swfolder = ['388', '438', '508']
            for sw in swfolder:
                dir_post_sw = dir_post_d + '\\' + sw
                originexport(dir_post_sw)
input("全部完成，输入回车关闭程序")