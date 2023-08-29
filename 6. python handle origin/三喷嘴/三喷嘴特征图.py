import originpro as op
import os


def originexport(dir_post):
    '''
    读取并导出图片
    '''
    files = os.listdir(dir_post)
    opjufiles = []
    for file in files:
        if '.opju' in file:
            opjufiles.append(file)
    for opjufile in opjufiles:
        src_opju = dir_post + '\\' + opjufile
        op.open(file = src_opju, readonly = False)
        gp = op.find_graph('Graph1')
        exp_file = src_opju.replace('.opju', '.png')
        gp.save_fig(path=exp_file, type='png', width=1500)
        print(f'Graph exported: {exp_file}')
    op.save(src_opju)


if __name__ == "__main__":
    # 定义计算根目录
    dir_post1 = "E:\\0-PhD\\3 nozzle\\本章图片\\变间距"
    originexport(dir_post1)
    dir_post2 = "E:\\0-PhD\\3 nozzle\\本章图片\\变旋流"
    originexport(dir_post2)
input("全部完成，输入回车关闭程序")