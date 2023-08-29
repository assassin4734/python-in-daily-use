import pandas as pd
'''
处理火焰散点数据
1. 热扩散率alpha=0.000195
2. 层流火焰传播速度sl=0.29
3. 湍流强度ti=0.05
'''


def coldflowfield(sw):
    '''
    tfs为湍流火焰传播速度
    mv为速度
    '''
    dir_cold_scale = dir_cold_d + '\\' + sw + '\\' + str(scale)
    dir_data = dir_cold_scale + '\\data.xlsx'
    ori = pd.read_excel(dir_data)
    # 取值
    tfs = ori.iloc[:, 0]
    mv = ori.iloc[:, 1]
    return tfs, mv, dir_cold_scale


def var(tfs, mv, dirc):
    '''
    计算关键物理量
    alpha为热扩散率
    tts为湍流时间尺度
    cts为化学时间尺度
    tls为湍流长度尺度
    x为横坐标，是湍流尺度与层流火焰厚度的比
    y为纵坐标，是脉动速度和层流火焰传播速度的比
    '''
    cts_value = alpha/(sl**2)
    # 定义出用来储存的列表
    cts = []
    tts = []
    tls = []
    x = []
    y = []
    # 遍历运算
    for lo in range(len(tfs)):
        cts.append(cts_value)
        # 计算湍流时间尺度
        tts_value = ((tfs[lo]/0.52/(mv[lo]*ti))**4)*cts_value
        tts.append(tts_value)
        # 计算湍流长度尺度
        tls_value = mv[lo]*ti*tts_value
        tls.append(tls_value)
        # 计算横坐标
        x_value = tls_value/(2*alpha/sl)
        x.append(x_value)
        # 计算纵坐标
        y_value = mv[lo]*ti/sl
        y.append(y_value)
    # 组合成新表
    df = pd.DataFrame({'turbulent flame speed': tfs, 'velocity magnitude': mv,
                      'chemical time scale': cts, 'turbulence time scale': tts, 
                      'turbulence length scale': tls, '湍流尺度与层流火焰厚度之比': x, '脉动速度和层流火焰传播速度之比': y})
    df.to_excel(dirc+'\\计算完成的值.xlsx', index=False)
    print(dirc + ' 计算完成')


if __name__ == "__main__":
    # 定义物理量
    alpha = 0.000195
    sl = 0.29
    ti = 0.05
    # 定义计算根目录
    dir_cold = "E:\\0-PhD\\3 nozzle\\coldflowfield\\postprocessing\\"
    # 定义目录变量
    distance_folder = ['1925', '1625', '2250']
    scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
    #
    print('# 找到工作目录')
    #
    for scale in scale_factor:
        for di in range(len(distance_folder)):
            # G:\\assassin\\3nozzle\\1625
            distance = distance_folder[di]
            # 定义新目录
            dir_cold_d = dir_cold + distance
            # 变间距目录
            # G:\\assassin\\3nozzle\\1625\\388
            if distance != '1925':
                sw = '438'
                tfs, mv, dirc = coldflowfield(sw)
                var(tfs, mv, dirc)
            else:
                swfolder = ['388', '438', '508']
                for sw in swfolder:
                    tfs, mv, dirc = coldflowfield(sw)
                    var(tfs, mv, dirc)
print('全部完成')
