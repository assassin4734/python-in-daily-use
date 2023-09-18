import numpy as np
import pandas as pd
import scipy.interpolate


pd.set_option("mode.chained_assignment", None)


# 主函数
def pod_decomposition_and_reconstruction():
    '''
    进行POD分解
    '''
    print('开始pod分解\n')
    print("# 定义两个dataframe储存两个方向的速度")
    u_velocity = pd.DataFrame()
    v_velocity = pd.DataFrame()
    print("# 读取不同截面的dat")
    # 按照plane分类，把不同缩放因子的dat都读出来
    for plane in planes:
        # 按照plane分类定义名称，不同截面的变量名称存在txt文件里，读进来转化成列表
        # V29是轴向坐标
        global y_cor, x_cor
        y_cor = 'V29'
        if plane == 'plane3':
            varname = [v.replace('\n', '') for v in list(open(dir + 'plane3.txt'))]
            x_cor = 'dimensionless X2'
            start = 43
            end = 40043
        else:
            varname = [v.replace('\n', '') for v in list(open(dir + 'plane1&2.txt'))]
            x_cor = 'V28'
            start = 38
            end = 40038
        # 开始按缩放因子遍历
        for num in range(len(scale_factor)):
            str_factors = str(scale_factor[num])
            # 按缩放因子读对应的dat
            dir_data = dir_post_n + str_factors + '\\' + plane + '.dat'
            print(dir_data + '正被处理\n')
            print("# 生成两个速度的矩阵")
            ori_data = pd.read_csv(dir_data, sep=' ', dtype=np.float64, skiprows=start, names=varname)
            # 这里保证列标签一致才能相加，记住v是被加到u的下面的
            print(ori_data)
            # V30是轴向速度 V31是径向速度
            u_velocity["data-"+str(num+1)] = ori_data["V30"]
            v_velocity["data-"+str(num+1)] = ori_data["V31"]
            print('# 定义一个坐标矩阵')
            global coordinate
            coordinate = pd.concat([ori_data[x_cor], ori_data[y_cor]], axis=1)
            # print(coordinate)
            # 进行速度数据的POD分解处理
        lsm, svm, rsm = pod_dealwith_velocitydat(u_velocity, v_velocity)
        # 进行特征值的计算
        singular_value_save(plane, svm)
        # 进行模态的计算
        mode_cal(start, end, plane, uv_matrix, lsm)
        # 进行速度的重构
        pod_reconstruction(start, end, plane)


def pod_dealwith_velocitydat(u_velocity, v_velocity):
    '''
    处理已经提取完成的速度矩阵
    '''    
    print("# 合并矩阵，合并之后的矩阵是纵向的")
    global uv_matrix
    uv_matrix = pd.concat([u_velocity, v_velocity], axis=0)
    print(uv_matrix)
    print('# 求快照pod的特征方阵')
    # 暂时用10替代
    C_snap_pod = (uv_matrix.T.dot(uv_matrix)).divide(10)
    print('# 进行pod分解')
    lsm, svm, rsm = np.linalg.svd(C_snap_pod)
    print('# 把特征值储存，然后求特征能量占比，也同样储存')
    return lsm, svm, rsm


def singular_value_save(plane, svm):
    # 特征值储存
    singular_value = open(dir_pod_matrix + plane + '\\singular_value.txt', 'w', encoding='utf-8')
    # 把svm中的值转化为字符串
    svm_str = list(map(str, svm))
    singular_value.writelines(svm_str)
    singular_value.write('\n')
    total_singular_value = 0
    n = 1
    for i in svm:
        total_singular_value += i
    singular_value.write("总能量为：" + str(total_singular_value) + '\n')
    for i in svm:
        singular_value.write(str(i) + "  " + str(n) + "阶能量占比为：" +
                str(i/total_singular_value*100) + '\n')
        n += 1
    singular_value.close()


def mode_cal(start, end, plane, uv_matrix, lsm):
    global phi_velocity
    phi_velocity = uv_matrix.dot(lsm)
    print('# 保存pod分解的特征速度结果')
    # 暂时用10替代
    for num in range(0, 9):
        mode_name = dir_pod_matrix + plane + '\\' + str(num) + "th_mode.dat"
        # 求归一化的基准以及归一化
        phi_nor = 0
        nor_vector = phi_velocity.iloc[:, num]
        for ele in nor_vector:
            phi_nor = phi_nor + ele ** 2
        phi_nor = phi_nor ** 0.5
        phi_velocity.iloc[:, num] = nor_vector.divide(phi_nor)
        # 求归一化后的u速度特征向量
        u_vector = (phi_velocity.head(end-start)[num])
        # 求归一化后的v速度特征向量
        v_vector = (phi_velocity.tail(end-start)[num])
        # 合并两个速度特征向量
        pod_uv_matrix = pd.concat([u_vector, v_vector], axis=1)
        # 与坐标一起合并
        pod_matrix = pd.concat([coordinate, pod_uv_matrix], axis=1)
        # 保存结果
        pod_matrix.to_csv(mode_name, sep=' ', index=False, header=None)
        with open(mode_name, 'r+', encoding='utf-8') as f:
            content = f.read()
            f.seek(0, 0)
            f.write('TITLE     = "Tecplot Export"\nVARIABLES = "'+x_cor+'"\n"'+y_cor+'"\n"V30"\n"V31"\nZONE T="Rectangular zone"\n STRANDID=0, SOLUTIONTIME=0\n I=200, J=200, K=1, ZONETYPE=Ordered\n DATAPACKING=POINT\n DT=(SINGLE SINGLE SINGLE SINGLE )\n' + content)
            f.close()


def pod_reconstruction(start, end, plane):
    '''
    进行重构
    '''
    print('# 进行缩放因子的拟合,先求缩放因子特征矩阵')
    scale_coe = uv_matrix.T.dot(phi_velocity)
    print("缩放因子特征矩阵")
    print(scale_coe)
    print('# 定义出缩放因子拟合矩阵')
    # 样本的特征向量是按行排列的
    scale_coe_new = pd.DataFrame()
    print('# 按样本数来插值')
    # 先用10替代
    scale_ori = np.linspace(start=0.1, stop=1, num=10)
    new_scale_list = np.linspace(start=0.1, stop=1, num=num_of_scale)
    print('# 新的缩放因子组')
    print(new_scale_list)
    scale_new = new_scale_list
    for num in range(0, 10):
        # 行索引，按行去拟合
        y = scale_coe.iloc[:, num].values
        func = scipy.interpolate.interp1d(scale_ori, y, kind='quadratic')
        scale_coe_newvector = pd.DataFrame(func(scale_new))
        scale_coe_new = pd.concat(
            [scale_coe_new, scale_coe_newvector], axis=1)
    print("旧的特征速度矩阵")
    print(phi_velocity)
    scale_coe_new = scale_coe_new.T
    scale_coe_new.index = list(phi_velocity)
    print("拟合后的缩放因子特征矩阵")
    # 拟合之后按列排布了
    print(scale_coe_new)
    scale_coe_new.to_excel(dir_re_matrix + plane + '\\scale_coe_new.xlsx')
    scale_coe_trans = scale_coe.T
    scale_coe_trans.to_excel(dir_re_matrix + plane + '\\scale_coe_ori.xlsx')
    print('# 用新的缩放因子组，求出新的特征速度矩阵')
    uv_matrix_new = phi_velocity.dot(scale_coe_new)
    print(uv_matrix_new)
    for mark in range(0, num_of_scale):
        re_name = dir_re_matrix + plane + '\\' + str(mark) + "-velocity.dat"
        # 求u速度特征向量
        u_vector = (uv_matrix_new.head(end-start)[mark])
        # 求v速度特征向量
        v_vector = (uv_matrix_new.tail(end-start)[mark])
        # 合并两个速度特征向量
        pod_uv_matrix = pd.concat([u_vector, v_vector], axis=1)
        # 与坐标一起合并
        pod_matrix = pd.concat([coordinate, pod_uv_matrix], axis=1)
        # 保存结果
        pod_matrix.to_csv(re_name, sep=' ', index=False, header=None)
        with open(re_name, 'r+', encoding='utf-8') as f:
            content = f.read()
            f.seek(0, 0)
            f.write('TITLE     = "Tecplot Export"\nVARIABLES = "'+x_cor+'"\n"'+y_cor+'"\n"V30"\n"V31"\nZONE T="Rectangular zone"\n STRANDID=0, SOLUTIONTIME=0\n I=200, J=200, K=1, ZONETYPE=Ordered\n DATAPACKING=POINT\n DT=(SINGLE SINGLE SINGLE SINGLE )\n' + content)
            f.close()


if __name__ == "__main__":
    '''
    程序主体
    '''
    print('定位后处理的目录')
    nozzle_folder = ['5nozzle', '3nozzle', '1nozzle']
    scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
    dir = 'E:\\0-PhD\\5 nozzle\\0-5NOZZLE-DLN2.6SIZE\\postprocessing\\'
    num_of_scale = int(input("输入想要拟合的缩放因子数量："))
    planes = ['plane1', 'plane2', 'plane3']
    for num1 in range(len(nozzle_folder)):
        # G:\\assassin\\3nozzle\\1625
        nozzle = nozzle_folder[num1]
        dir_post_n = dir + nozzle + '\\48\\48-'
        # 定义POD结果保存位置
        dir_pod_matrix = dir + nozzle + '\\pod_results\\'
        dir_re_matrix = dir + nozzle + '\\pod_reconstruct\\'
        pod_decomposition_and_reconstruction()
    input("POD分解与重构已经完成")