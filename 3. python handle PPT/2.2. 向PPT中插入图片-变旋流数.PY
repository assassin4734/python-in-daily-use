# -encoding utf-8-

'''
1. 将数值模拟得到的图片插入PPT中
2. 按图片类型插入到PPT的不同页上
3. 用win32api模块重写
'''


import win32com.client as client


def input_function():
    act_str = input("请输入图片名称:\n0: velocity-cut.tiff\n1: ch+-cut.tiff\n2: flame-cut.tiff\n")
    if act_str == "0":
        photo_name = 'velocity-cut.tiff'
        return(photo_name)
    elif act_str == "1":
        photo_name = 'ch+-cut.tiff'
        return(photo_name)
    elif act_str == "2":
        photo_name = 'flame-cut.tiff'
        return(photo_name)
    else:
        print("input error!")
        input_function()


# 实例化一个ppt演示文稿
PPT = client.GetActiveObject("Powerpoint.Application")
PPTPres = PPT.ActivePresentation
print("共有" + str(len(PPTPres.Slides)) + "张slide")
# 定义磅值与厘米的换算基准
unit_point = 0.03527
# 定义目录
swirl_folder = ["28.5", "35.5", "40.5", "45.5", "52.5"]
scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]
# 图片名称
photos = input_function()
# 定义图片大小（也通过它来定义位置）
print('火焰结构和反应区的图片宽度是3.28厘米，速度分布的图片宽度是7厘米')
ph_width = float(input('输入图片宽度：'))
print('火焰结构和反应区的图片高度是3.87厘米，速度分布的图片高度是3.87厘米')
ph_height = float(input('输入图片高度：'))
print('火焰结构和反应区的横向间距是3.28厘米，速度分布的横向间距是7厘米')
ph_line = float(input('输入横向间距:'))
print('火焰结构和反应区的纵向间距是4.17厘米，速度分布的横向间距是3.87厘米')
ph_col = float(input('输入纵向间距:'))
#定义PPT的页数
i = int(input("请输入PPT的起始页码（0为首张）"))
# 定义换行图片数
j = int(input("请输入换行图片数（整数）"))
for swirl in swirl_folder:
    # E:\\0-PhD\\1 nozzle\\different swirl number\\postprocessing
    dir_eq = 'E:\\0-PhD\\1 nozzle\\different swirl number\\postprocessing\\z-' + str(swirl)
    # 横向的起始位置
    x_position = 0
    # 纵向的起始位置
    y_position = 0
    print(dir_eq + ' is on processing')
    for num in range(len(scale_factor)):
        str_factors = str(scale_factor[num]) 
        #  E:\\0-PhD\\1 nozzle\\different swirl number\\postprocessing\\z-28.5\\28.5-0.1
        dir_scale = dir_eq + '\\' + str(swirl) + '-' + str_factors
        print(dir_scale + ' is on going')
        #  E:\\0-PhD\\1 nozzle\\different swirl number\\postprocessing\\z-28.5\\28.5-0.1\\velocity-cut.tiff
        photo_position = dir_scale + '\\' + photos
        print(photo_position)
        # 插入图片
        image = PPTPres.Slides[i].Shapes.AddPicture(FileName=photo_position, LinkToFile=False,
                                                    SaveWithDocument=True, Left=x_position, Top=y_position,
                                                    Width=ph_width/unit_point, Height=ph_height/unit_point)
        x_position += ph_line/unit_point
        # 图片换行
        if (num+1) % j == 0:
            x_position = 0
            y_position += ph_col/unit_point
    # 换页
    i += 1
input("all done, press enter to exit")