# -encoding utf-8-

'''
1. 将数值模拟得到的图片插入PPT中
2. 按图片类型插入到PPT的不同页上
3. 用win32api模块重写
'''


import win32com.client as client
   

if __name__ == "__main__":
    # 实例化一个ppt演示文稿
    PPT = client.GetActiveObject("Powerpoint.Application")
    PPTPres = PPT.ActivePresentation
    print("共有" + str(len(PPTPres.Slides)) + "张slide")
    # 定义磅值与厘米的换算基准
    unit_point = 0.03527
    # 定义图片大小（也通过它来定义位置）
    print('central的图片宽度是1.5厘米')
    ph_width = float(input('输入图片宽度：'))
    print('central的图片高度是2.72厘米')
    ph_height = float(input('输入图片高度：'))
    print('central的图片横向间距是1.6厘米')
    ph_line = float(input('输入横向间距:'))
    print('central的图片纵向间距是2.82厘米')
    ph_col = float(input('输入纵向间距:'))
    # 定义PPT的页数
    i = int(input("请输入PPT的起始页码（0为首张）"))
    # 定义换行图片数
    j = int(input("请输入换行图片数（整数）"))
    # 定义计算根目录
    dir_post = "E:\\0-PhD\\3 nozzle\\postprocessing\\"
    # 定义目录变量
    distance_folder = ['2250', '1925', '1625']
    scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
    #
    print('# 找到工作目录')
    # 横向的起始位置
    x_position = 0
    # 纵向的起始位置
    y_position = 0
    #
    for num1 in range(len(distance_folder)):
        # G:\\assassin\\3nozzle\\1625
        distance = distance_folder[num1]
        dir_post_d = dir_post + distance
        # 变间距目录
        # G:\\assassin\\3nozzle\\1625\\388
        sw = '438'
        dir_post_sw = dir_post_d + '\\' + sw + '\\'
        for num2 in range(len(scale_factor)):
            str_factors = str(scale_factor[num2])
            dir_post_ph = dir_post_sw + str_factors + '\\central-streamline-cut.png'
            print(dir_post_ph)
            # 插入图片
            PPTPres.Slides[i].Shapes.AddPicture(FileName=dir_post_ph, LinkToFile=False,
                                                SaveWithDocument=True, Left=x_position, Top=y_position,
                                                Width=ph_width/unit_point, Height=ph_height/unit_point)
            x_position += ph_line/unit_point
        x_position = 0
        y_position += ph_col/unit_point
print('all done')
