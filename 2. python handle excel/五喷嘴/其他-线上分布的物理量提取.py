import pandas as pd


def pullandmerge(key):
    '''
    先把特征位置循环定义出来，然后再遍历缩放因子
    '''
    for i in range(3):
        plane_name = '-plane-' + str(i+1) + '.csv'
        for j in range(4):
            csv_name = str((j+1)*0.5) + plane_name
            # 来一个对应位置的存储
            df = pd.DataFrame()
            # 定义缩放因子对的变量和目录
            for num2 in range(len(scale_factor)):
                str_factors = str(scale_factor[num2])
                dir_post_scale = dir_post_n + str_factors + '\\' + csv_name
                print(dir_post_scale + ' 正在处理')
                df_scale = pd.read_csv(dir_post_scale)
                print(df_scale[key])
                df.insert(loc=num2, value=df_scale[key], allow_duplicates=True, column=str_factors)
            if i == 2:
                df.insert(loc=0, value=df_scale['dimensionless X2'], allow_duplicates=True, column='dimensionless X2')
                df.to_excel(dir_post+nozzle+'\\48\\'+key+'-'+csv_name.replace('.csv', '.xlsx'))
            else:
                df.insert(loc=0, value=df_scale['V28'], allow_duplicates=True, column='V28')
                df.to_excel(dir_post+nozzle+'\\48\\'+key+'-'+csv_name.replace('.csv', '.xlsx'))


if __name__ == "__main__":
    # 定义想要的变量
    # key = input('输入想要的变量：')
    key = 'dimensionless q'
    # 定义计算根目录
    dir = "E:\\0-PhD\\5 nozzle\\0-5NOZZLE-DLN2.6SIZE\\"
    dir_post = dir + "postprocessing\\"
    # 定义目录变量
    nozzle_folder = ['5nozzle', '3nozzle', '1nozzle']
    scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
    #
    print('# 找到工作目录')
    #
    for num1 in range(len(nozzle_folder)):
        # G:\\assassin\\3nozzle\\1625
        nozzle = nozzle_folder[num1]
        dir_post_n = dir_post + nozzle + '\\48\\48-'
        pullandmerge(key)
