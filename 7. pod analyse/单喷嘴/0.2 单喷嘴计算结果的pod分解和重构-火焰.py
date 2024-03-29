import os
import re
import numpy as np
import pandas as pd
import scipy.interpolate


pd.set_option("mode.chained_assignment", None)


def choosing(display_str):
    print("-" * 20)
    print(display_str)
    print("exit退出")
    print("-" * 20)
    action_str = input()
    try:
        if action_str.isnumeric() == True:
            return int(action_str)
        else:
            print("输入错误，请重新输入")
            choosing(display_str)
    except:
        if action_str == 'exit':
            os._exit(0)
        print("编号输入错误，请重新输入")
        choosing(display_str)


print('定位后处理的目录')
onenozzlefolder = {'变当量比': 'eq\\postprocessing-transport\\',
                   '变旋流数': 'different swirl number\\postprocessing\\'}
folder = {'sw_folder': ["z-28.5", "z-35.5", "z-45.5", "z-52.5"],
          'eq_folder': ["eq=0.55", "eq=0.65", "eq=0.75", "eq=0.85", "eq=0.95"]}
scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3]
dir = 'E:\\0-PhD\\1 nozzle\\'
num_of_scale = int(input("输入想要拟合的缩放因子数量："))
start = choosing("输入数据的起始行：")
end = choosing("输入数据的结束行：")

for para in onenozzlefolder:
    # E:\\0-PhD\\1 nozzle\\eq\\postprocessing\\
    dir_para = dir + onenozzlefolder[para]
    print(dir_para + '正被处理')
    if para == '变当量比':
        fol = 'eq_folder'
    elif para == '变旋流数':
        fol = 'sw_folder'
    else:
        pass
    for var in folder[fol]:
        # E:\\0-PhD\\1 nozzle\\eq\\postprocessing\\eq=0.55\\pod_analyse\\'
        dir_pod = dir_para + var + '\\pod_analyse\\'
        print(dir_pod + '正被处理\n')
        print('开始pod分解\n')
        print("# 定义一个dataframe储存反应进度变量")
        premixc = pd.DataFrame()
        print("# 生成反应进度变量矩阵")
        dat_file = []
        dats = os.listdir(dir_pod)
        for file in dats:
            if re.search(".dat", file, re.I):
                dat_file.append(file)
        for dat in dat_file:
            print(dat)
        for dat in dat_file:
            num = dat_file.index(dat)
            # E:\\0-PhD\\1 nozzle\\eq\\postprocessing\\28.5\\pod_analyse\\
            dir_data = dir_pod + dat
            row = pd.read_csv(dir_data, sep=' ', dtype=np.float64, skiprows=start, names=[
                "premixc", "y coordinate", "z coordinate", "z velocity", "y velocity"])
            # 这里保证列标签一致才能相加，记住v是被加到u的下面的
            print(row)
            premixc["data-"+str(num+1)] = row["premixc"]
        print('# 定义一个坐标矩阵')
        coordinate = pd.concat(
            [row["y coordinate"], row["z coordinate"]], axis=1)
        print(coordinate)
        print('# 求快照pod的特征方阵')
        C_snap_pod = (premixc.T.dot(premixc)).divide(len(dat_file))
        print('# 进行pod分解')
        lsm, svm, rsm = np.linalg.svd(C_snap_pod)
        print('# 把特征值储存，然后求特征能量占比，也同样储存')
        # 定义保存位置
        try:
            os.makedirs(dir_pod + 'pod_results-flame\\')
            dir_pod_matrix = dir_pod + 'pod_results-flame\\'
        except:
            dir_pod_matrix = dir_pod + 'pod_results-flame\\'
        k = open(dir_pod_matrix + 'singular_value.txt', 'w', encoding='utf-8')
        # 把svm中的值转化为字符串
        svm_str = list(map(str, svm))
        k.writelines(svm_str)
        k.write('\n')
        total_singular_value = 0
        n = 1
        for i in svm:
            total_singular_value += i
        k.write("总能量为：" + str(total_singular_value) + '\n')
        for i in svm:
            k.write(str(i) + "  " + str(n) + "阶能量占比为：" +
                    str(i/total_singular_value*100) + '\n')
            n += 1
        k.close()
        phi_premixc = premixc.dot(lsm)
        print('# 保存pod分解的特征速度结果')
        for num in range(0, len(dat_file)):
            mode_name = dir_pod_matrix + str(num) + "th_mode.dat"
            # 求归一化的基准以及归一化
            phi_nor = 0
            nor_vector = phi_premixc.iloc[:, num]
            for ele in nor_vector:
                phi_nor = phi_nor + ele ** 2
            phi_nor = phi_nor ** 0.5
            phi_premixc.iloc[:, num] = nor_vector.divide(phi_nor)
            # 求归一化后的反应进度变量特征向量
            premixc_vector = (phi_premixc.head(end-start)[num])
            # 与坐标一起合并
            pod_matrix = pd.concat([coordinate, premixc_vector], axis=1)
            # 保存结果
            pod_matrix.to_csv(mode_name, sep=' ', index=False, header=None)
            with open(mode_name, 'r+', encoding='utf-8') as f:
                content = f.read()
                f.seek(0, 0)
                f.write('''TITLE     = "Tecplot Export"\nVARIABLES = "V28"\n"V29"\n"premixc"\nZONE T="Rectangular zone"\n STRANDID=0, SOLUTIONTIME=0\n I=200, J=200, K=1, ZONETYPE=Ordered\n DATAPACKING=POINT\n DT=(SINGLE SINGLE SINGLE SINGLE )\n''' + content)
                f.close()
        print('# 进行缩放因子的拟合,先求缩放因子特征矩阵')
        scale_coe = premixc.T.dot(phi_premixc)
        print("缩放因子特征矩阵")
        print(scale_coe)
        print('# 定义出缩放因子拟合矩阵')
        # 样本的特征向量是按行排列的
        scale_coe_new = pd.DataFrame()
        print('# 按样本数来插值')
        scale_ori = np.linspace(start=0.1, stop=1, num=len(dat_file))
        new_scale_list = np.linspace(start=0.1, stop=1, num=num_of_scale)
        print('# 新的缩放因子组')
        print(new_scale_list)
        scale_new = new_scale_list
        for num in range(0, len(dat_file)):
            # 行索引，按行去拟合
            y = scale_coe.iloc[:, num].values
            func = scipy.interpolate.interp1d(scale_ori, y, kind='quadratic')
            scale_coe_newvector = pd.DataFrame(func(scale_new))
            scale_coe_new = pd.concat(
                [scale_coe_new, scale_coe_newvector], axis=1)
        print("旧的特征速度矩阵")
        print(phi_premixc)
        scale_coe_new = scale_coe_new.T
        scale_coe_new.index = list(phi_premixc)
        print("拟合后的缩放因子特征矩阵")
        # 拟合之后按列排布了
        print(scale_coe_new)
        # 定义保存位置
        try:
            os.makedirs(dir_pod + 'pod_reconstructs-flame\\')
            dir_re_matrix = dir_pod + 'pod_reconstructs-flame\\'
        except:
            dir_re_matrix = dir_pod + 'pod_reconstructs-flame\\'
        scale_coe_new.to_excel(dir_re_matrix + 'scale_coe_new.xlsx')
        scale_coe_trans = scale_coe.T
        scale_coe_trans.to_excel(dir_re_matrix + 'scale_coe_ori.xlsx')
        print('# 用新的缩放因子组，求出新的反应进度变量矩阵')
        premixc_new = phi_premixc.dot(scale_coe_new)
        print(premixc_new)
        for mark in range(0, num_of_scale):
            re_name = dir_re_matrix + str(mark) + "-flame.dat"
            # 求归一化后的u速度特征向量
            premixc_new_vector = (premixc_new.head(end-start)[mark])
            # 与坐标一起合并
            pod_matrix = pd.concat([coordinate, premixc_new_vector], axis=1)
            # 保存结果
            pod_matrix.to_csv(re_name, sep=' ', index=False, header=None)
            with open(re_name, 'r+', encoding='utf-8') as f:
                content = f.read()
                f.seek(0, 0)
                f.write('''TITLE     = "Tecplot Export"\nVARIABLES = "V28"\n"V29"\n"premixc"\nZONE T="Rectangular zone"\n STRANDID=0, SOLUTIONTIME=0\n I=200, J=200, K=1, ZONETYPE=Ordered\n DATAPACKING=POINT\n DT=(SINGLE SINGLE SINGLE SINGLE )\n''' + content)
                f.close()
input("POD分解与重构已经完成")
