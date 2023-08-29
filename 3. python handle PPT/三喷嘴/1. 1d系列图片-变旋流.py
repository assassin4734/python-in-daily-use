# -encoding utf-8-

'''
1. 将数值模拟得到的图片插入PPT中
2. 按图片类型插入到PPT的不同页上
3. 用win32api模块重写
'''


import win32com.client as client


def input_function():
    act_str = input(
        "请输入图片名称:\n0: 0.75d-p-cut.png\n1: 0.75d-q-cut.png\n2: 0.75d-vorticity-cut.png\n")
    if act_str == "0":
        photo_name = '0.75d-p-cut.png'
        return(photo_name)
    elif act_str == "1":
        photo_name = '0.75d-q-cut.png'
        return(photo_name)
    elif act_str == "2":
        photo_name = '0.75d-vorticity-cut.png'
        return(photo_name)
    else:
        print("input error!")
        input_function()


if __name__ == "__main__":
    # 实例化一个ppt演示文稿
    PPT = client.GetActiveObject("Powerpoint.Application")
    PPTPres = PPT.ActivePresentation
    print("共有" + str(len(PPTPres.Slides)) + "张slide")
    phname = input_function()
    # 定义磅值与厘米的换算基准
    unit_point = 0.03527
    # 定义图片大小（也通过它来定义位置）
    print('图片宽度是4.9厘米')
    ph_width = 4.9
    print('图片高度是2厘米')
    ph_height = 2
    print('central的图片横向间距是5.1厘米')
    ph_line = 5.1
    print('central的图片纵向间距是2.2厘米')
    ph_col = 2.2
    # 定义PPT的页数
    i = int(input("请输入PPT的起始页码（0为首张）"))
    # 定义换行图片数
    j = 1
    # 定义计算根目录
    dir_post = "E:\\0-PhD\\3 nozzle\\postprocessing\\1925\\"
    # 定义目录变量
    sw_folder = ['388', '438', '508']
    scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
    #
    print('# 找到工作目录')
    # 横向的起始位置
    x_position = 1.74/unit_point
    # 纵向的起始位置
    y_position = 1.75/unit_point
    #
    for num1 in range(len(sw_folder)):
        # G:\\assassin\\3nozzle\\1625
        sw = sw_folder[num1]
        dir_post_sw = dir_post + sw + '\\'
        # 变间距目录
        # G:\\assassin\\3nozzle\\1625\\388
        for num2 in range(len(scale_factor)):
            str_factors = str(scale_factor[num2])
            dir_post_ph = dir_post_sw + str_factors + '\\' + phname
            print(dir_post_ph)
            # 插入图片
            PPTPres.Slides[i].Shapes.AddPicture(FileName=dir_post_ph, LinkToFile=False,
                                                SaveWithDocument=True, Left=x_position, Top=y_position,
                                                Width=ph_width/unit_point, Height=ph_height/unit_point)
            y_position += ph_col/unit_point
        y_position = 1.75/unit_point
        x_position += ph_line/unit_point
print('all done')
