# -encoding utf-8-

'''
1. 将数值模拟得到的图片插入PPT中
2. 按图片类型插入到PPT的不同页上
3. 用win32api模块重写
'''


import win32com.client as client


# 实例化一个ppt演示文稿
PPT = client.GetActiveObject("Powerpoint.Application")
PPTPres = PPT.ActivePresentation
print("共有" + str(len(PPTPres.Slides)) + "张slide")
# 定义磅值与厘米的换算基准
unit_point = 0.03527
# 定义目录
eq_folder = ["eq=0.55", "eq=0.65", "eq=0.75", "eq=0.85", "eq=0.95"]
scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]
photos = input("请输入图片名称（带扩展名）")
# 定义图片大小（也通过它来定义位置）
print('火焰结构和反应区的图片宽度是3.28厘米，速度分布的图片宽度是7厘米')
ph_width = float(input('输入图片宽度：'))
print('火焰结构和反应区的图片高度是3.87厘米，速度分布的图片高度是3.87厘米')
ph_height = float(input('输入图片高度：'))
#定义PPT的页数
i = int(input("请输入PPT的起始页码（0为首张）"))
# 定义换行图片数
j = int(input("请输入换行图片数（整数）"))
for folders in eq_folder:
    # 地址格式举例：F:\\PhD\\1 nozzle\\eq\\postprocessing\\eq=0.55
    dir_colletion = 'F:\\PhD\\1 nozzle\\eq\\postprocessing\\' + folders
    print(dir_colletion + ' is on processing')
    # 横向的起始位置
    x_position = 0
    # 纵向的起始位置
    y_position = 0
    for num in range(len(scale_factor)):
        factors = scale_factor[num]
        str_factors = str(factors) 
        # 地址格式举例：F:\\PhD\\1 nozzle\\eq\\postprocessing\\eq=0.55\\40.5-1
        dir_position = dir_colletion + '\\40.5-' + str_factors
        print(dir_position + ' is on going')
        photo_position = dir_position + '\\' + photos
        print(photo_position)
        # 插入图片
        image = PPTPres.Slides[i].Shapes.AddPicture(FileName=photo_position, LinkToFile=False,
                                                    SaveWithDocument=True, Left=x_position, Top=y_position,
                                                    Width=ph_width/unit_point, Height=ph_height/unit_point)
        x_position += ph_width/unit_point
# 图片换行
        if (num+1) % j == 0:
            x_position = 0
            y_position += ph_height/unit_point
    # 换页
    i += 1
input("all done, press enter to exit")