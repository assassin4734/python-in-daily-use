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
        exp_file = dir_post + nozzle + '-' + plane + '.png'
        gp.save_fig(path=exp_file, type='png', width=1500)
        print(f'Graph exported: {exp_file}')
    op.save(src_opju)



if __name__ == "__main__":
    '''
    程序主体
    '''
    print('定位后处理的目录')
    nozzle_folder = ['5nozzle', '3nozzle', '1nozzle']
    dir = 'E:\\0-PhD\\5 nozzle\\0-5NOZZLE-DLN2.6SIZE\\postprocessing\\'
    planes = ['plane1', 'plane2', 'plane3']
    for nozzle in nozzle_folder:
        for plane in planes:
            dir_1 = dir + nozzle + '\\pod_reconstruct-ch2o\\' + plane + '\\'
            originexport(dir_1)
            dir_2 = dir + nozzle + '\\pod_reconstruct\\' + plane + '\\'
            originexport(dir_2)

    
    input("导出已经完成")