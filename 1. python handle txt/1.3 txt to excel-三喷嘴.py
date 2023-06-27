# _*_ encoding utf-8 _*_
# 将txt文件转为xls格式


import pandas as pd


def change(dir_post_sw_f):
    """
    将指定文件夹目录下的txt转化为xls
    :param current_file:指定目录下的文件名
    :return:无
    """
    for num2 in range(len(scale_factor)):
        str_factors = str(scale_factor[num2])
        # 后处理地址
        dir_post_working = dir_post_sw_f + \
            str_factors + '\\' + name
        line_head = pd.DataFrame(["CoordinateX", "CoordinateY", "CoordinateZ", "ch2o", "Turbulent Energy Dissipation", "turbulent-flame-speed", "X Component Vorticity", "Temperature", "Y Component Vorticity", "stretch-fac", "helicity", "Z Component Vorticity", "oh", "X Component Velocity", "Pressure",
                    "Y Component Velocity", "Turbulent Kinetic Energy", "fmean", "Z Component Velocity", "premixc", "damkohler-number", "Magnitude Vorticity", "turb-intensity", "heat-release-rate", "Magnitude Velocity", "q-criterion", "raw-q-criterion", "无量纲Z", "无量纲Y", "轴向速度", "径向速度"]).T
        print(line_head)
        dat_to_excel = pd.read_csv(
            filepath_or_buffer=dir_post_working, skiprows=37, sep=' ', header=None, usecols=[i for i in range(1,32)])
        print(dat_to_excel)
        line_head.columns = dat_to_excel.columns
        extran = pd.concat([line_head, dat_to_excel], axis=0 ,ignore_index=True)
        print(extran)
        extran.to_excel(dir_post_working.replace('.dat', '.xlsx'))


if __name__ == "__main__":
    # 定义计算根目录
    dir_post = "E:\\0-PhD\\3 nozzle\\postprocessing\\"
    # 定义目录变量
    distance_folder = ['1625', '1925', '2250']
    scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
    name = 'interline.dat'
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
            dir_post_sw = dir_post_d + '\\' + sw + '\\'
            change(dir_post_sw)
        else:
            swfolder = ['388', '438', '508']
            for sw in swfolder:
                dir_post_sw = dir_post_d + '\\' + sw + '\\'
                change(dir_post_sw)
input("输入回车退出")
