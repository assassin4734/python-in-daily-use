import os
import numpy as np
import pandas as pd
from scipy.interpolate import interp1d


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


dir_pod = "E:\\1-python-in-daily-use\\7. pod analyse\\pod_data\\"
print("-" * len(dir_pod))
print(dir_pod)
print("-" * len(dir_pod))
start = choosing("输入数据的起始行：")
end = choosing("输入数据的结束行：")
pod_num = choosing("输入进行pod分解的数据文件个数: ")

print("# 定义两个dataframe储存两个方向的速度")
u_velocity = pd.DataFrame()
v_velocity = pd.DataFrame()

print("# 生成两个速度的矩阵")
for num in range(0, pod_num):
    data_name = str((num+1)*10) + ".txt"
    dir_data = dir_pod + data_name
    row = pd.read_csv(dir_data, sep=' ', dtype=np.float64, skiprows=start, names=[
                      "x coordinate", "z coordinate", "u velocity", "v velocity"])
    # 这里保证列标签一致才能相加，记住v是被加到u的下面的
    u_velocity["data-"+str(num+1)] = row["u velocity"]
    v_velocity["data-"+str(num+1)] = row["v velocity"]
print('# 定义一个坐标矩阵')
coordinate = pd.concat([row["x coordinate"], row["z coordinate"]], axis=1)
print("# 合并矩阵，合并之后的矩阵是纵向的")
uv_matrix = pd.concat([u_velocity, v_velocity], axis=0)
print('# 求快照pod的特征方阵')
C_snap_pod = (uv_matrix.T.dot(uv_matrix)).divide(pod_num)
print('# 进行pod分解')
lsm, svm, rsm = np.linalg.svd(C_snap_pod)
phi_velocity = uv_matrix.dot(lsm)
print('# 保存pod分解的特征速度结果')
for num in range(0, pod_num):
    # 定义保存位置
    dir_pod_matrix = "E:\\1-python-in-daily-use\\7. pod analyse\\pod_results\\" + \
        str(num+1) + "th_mode_phi.txt"
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
    pod_matrix.to_csv(dir_pod_matrix, sep=' ', index=False, header=None)
    with open(dir_pod_matrix, 'r+', encoding='utf-8') as f:
        content = f.read()
        f.seek(0, 0)
        f.write('VARIABLES = X,Y,phix,phiy\nZONE I=200,J=200,F=POINT \n' + content)
        f.close()
print('# 进行缩放因子的拟合,先求缩放因子特征矩阵')
scale_coe = uv_matrix.T.dot(phi_velocity)
print("缩放因子特征矩阵")
print(scale_coe)
print('# 定义出缩放因子拟合矩阵')
scale_coe_new = pd.DataFrame()
print('# 按样本数来插值')
scale_ori = np.linspace(start=0.02, stop=0.1, num=pod_num)
step_num = int(input("输入想要拟合的缩放因子数量："))
scale_new = np.linspace(start=0.02, stop=0.1, num=step_num)
for num in range(0, pod_num):
    y = scale_coe.iloc[:, num].values
    func = interp1d(scale_ori, y, kind='cubic')
    scale_coe_newvector = pd.DataFrame(func(scale_new))
    scale_coe_new = pd.concat([scale_coe_new, scale_coe_newvector], axis=1)
print("旧的特征速度矩阵")
print(phi_velocity)
scale_coe_new = scale_coe_new.T
scale_coe_new.index = list(phi_velocity)
print("拟合后的缩放因子特征矩阵")
print(scale_coe_new)
print('# 用新的缩放因子组，求出新的特征速度矩阵')
uv_matrix_new = phi_velocity.dot(scale_coe_new)
print(uv_matrix_new)
for mark in range(0, step_num):
    # 定义保存位置
    dir_re_matrix = "E:\\1-python-in-daily-use\\7. pod analyse\\pod_reconstruct\\" + \
        str(mark+1) + ".txt"
    # 求归一化后的u速度特征向量
    u_vector = (uv_matrix_new.head(end-start)[mark])
    # 求归一化后的v速度特征向量
    v_vector = (uv_matrix_new.tail(end-start)[mark])
    # 合并两个速度特征向量
    pod_uv_matrix = pd.concat([u_vector, v_vector], axis=1)
    # 与坐标一起合并
    pod_matrix = pd.concat([coordinate, pod_uv_matrix], axis=1)
    # 保存结果
    pod_matrix.to_csv(dir_re_matrix, sep=' ', index=False, header=None)
    with open(dir_re_matrix, 'r+', encoding='utf-8') as f:
        content = f.read()
        f.seek(0, 0)
        f.write('VARIABLES = X,Y,phix,phiy\nZONE I=200,J=200,F=POINT \n' + content)
        f.close()
input("POD分解与重构已经完成")
