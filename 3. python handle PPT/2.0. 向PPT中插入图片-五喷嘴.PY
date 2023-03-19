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
nozzles_folder = ['5nozzle', '3nozzle', '1nozzle']
distance_folder = ['48', '60', '72']
scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
# 图片名称
photos = input("请输入图片名称（带扩展名）")
# 定义图片大小（也通过它来定义位置）
print('火焰结构和反应区的图片宽度是3厘米，速度分布的图片宽度是7厘米')
ph_width = float(input('输入图片宽度：'))
print('火焰结构和反应区的图片高度是3.26厘米，速度分布的图片高度是4.17厘米')
ph_height = float(input('输入图片高度：'))
print('火焰结构和反应区的横向间距是3厘米，速度分布的横向间距是7厘米')
ph_line = float(input('输入横向间距:'))
print('火焰结构和反应区的纵向间距是3.99厘米，速度分布的横向间距是4.68厘米')
ph_col = float(input('输入纵向间距:'))
#定义PPT的页数
i = int(input("请输入PPT的起始页码（0为首张）"))
# 定义换行图片数
j = int(input("请输入换行图片数（整数）"))
for nozzles in nozzles_folder:
    # E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\5nozzle
    dir_nozzles = 'E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\postprocessing\\' + nozzles
    print(dir_nozzles + ' is on processing')
    for distance in distance_folder:
        # E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\5nozzle\\48
        dir_distance = dir_nozzles + '\\' + distance
        # 横向的起始位置
        x_position = 0
        # 纵向的起始位置
        y_position = 0
        for num in range(len(scale_factor)):
            str_factors = str(scale_factor[num]) 
            #  E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\5nozzle\\48\\48-1
            dir_scale = dir_distance + '\\' + distance + '-' + str_factors
            print(dir_scale + ' is on going')
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