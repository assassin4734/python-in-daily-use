import pandas as pd


def pullandmerge(key):
    '''
    先把特征位置循环定义出来，然后再遍历缩放因子
    '''
    csv_name = 'outlet-plane-1.csv'
    # 来一个对应位置的存储
    df = pd.DataFrame()
    # 定义缩放因子对的变量和目录
    for num2 in range(len(scale_factor)):
        vref = velocity[num2]
        str_factors = str(scale_factor[num2])
        dir_post_scale = dir_post_n + str_factors + '\\' + csv_name
        print(dir_post_scale + ' 正在处理')
        df_scale = pd.read_csv(dir_post_scale)
        print(df_scale[key])
        d_tfs = df_scale[key]/vref
        print(d_tfs)
        df.insert(loc=num2, value=d_tfs, allow_duplicates=True, column=str_factors)
    df.insert(loc=0, value=df_scale['V28'], allow_duplicates=True, column='V28')
    df.to_excel(dir_post+nozzle+'\\48\\'+key+'-'+csv_name.replace('.csv', '.xlsx'))


if __name__ == "__main__":
    # 定义想要的变量
    # key = input('输入想要的变量：')
    key = 'V30'
    # 定义计算根目录
    dir = "E:\\0-PhD\\5 nozzle\\0-5NOZZLE-DLN2.6SIZE\\"
    dir_post = dir + "postprocessing\\"
    # 定义目录变量
    nozzle_folder = ['5nozzle', '3nozzle', '1nozzle']
    scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
    velocity = [40.98, 36.88, 32.78, 28.68, 24.59, 18.44, 16.39, 14.34, 12.29, 10.24]
    #
    print('# 找到工作目录')
    #
    for num1 in range(len(nozzle_folder)):
        # G:\\assassin\\3nozzle\\1625
        nozzle = nozzle_folder[num1]
        dir_post_n = dir_post + nozzle + '\\48\\48-'
        pullandmerge(key)
