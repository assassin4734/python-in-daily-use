# -encoding utf-8-

'''
1. 将数值模拟得到的图片插入PPT中
2. 按图片类型插入到PPT的不同页上
3. 用win32api模块重写
'''


import win32com.client as client


def input_function():
    act_str = input("请输入图片名称:\n0: 无量纲轴向速度\n1: 无量纲径向速度\n2: turbulent-flame-speed\n")
    if act_str == "0":
        photo_name = '无量纲轴向速度'
        return(photo_name)
    elif act_str == "1":
        photo_name = '无量纲径向速度'
        return(photo_name)
    elif act_str == "2":
        photo_name = 'turbulent-flame-speed'
        return(photo_name)
    else:
        print("input error!")
        input_function()

def val_function():
    act_str = input("请输入变量名称:\n0: 变旋流数\n1: 变当量比")
    if act_str == "0":
        val_name = swirl_folder
        return(val_name)
    elif act_str == "1":
        val_name = eq_folder
        return(val_name)
    else:
        print("input error!")
        val_function()


# 实例化一个ppt演示文稿
PPT = client.GetActiveObject("Powerpoint.Application")
PPTPres = PPT.ActivePresentation
print("共有" + str(len(PPTPres.Slides)) + "张slide")
# 定义磅值与厘米的换算基准
unit_point = 0.03527
# 定义目录
swirl_folder = ["z-28.5", "z-35.5", "z-40.5", "z-45.5", "z-52.5"]
eq_folder = ["eq=0.55", "eq=0.65", "eq=0.75", "eq=0.85", "eq=0.95"]
positions = [10, 20, 40, 60]
# 图片名称
photos = input_function()
# 定义图片大小（也通过它来定义位置）
print('火焰传播速度的图片宽度是7.91厘米，线上速度分布的图片宽度是7.49厘米')
ph_width = float(input('输入图片宽度：'))
print('火焰传播速度的图片高度是5.72厘米，线上速度分布的图片高度是5.83厘米')
ph_height = float(input('输入图片高度：'))
print('线上速度分布的横向间距是7.91厘米，线上速度分布的横向间距是7.49厘米')
ph_line = float(input('输入横向间距:'))
print('火焰结构和反应区的纵向间距是6.34厘米，速度分布的横向间距是6.45厘米')
ph_col = float(input('输入纵向间距:'))
# 定义PPT的页数
i0 = int(input("请输入PPT的起始页码（0为首张）"))
# 定义换行图片数
j0 = int(input("请输入换行图片数（整数）"))
# 定义种类
variable = val_function()
# 横向的起始位置
x_position = 0
# 纵向的起始位置
y_position = 0
for v_num in range(len(variable)):
    v = variable[v_num]
    if variable == swirl_folder:
        # E:\\0-PhD\\1 nozzle\\different swirl number\\postprocessing
        dir = 'E:\\0-PhD\\1 nozzle\\different swirl number\\postprocessing\\' + v
    else:
        dir = 'E:\\0-PhD\\1 nozzle\\eq\\postprocessing\\' + v
        print(dir + ' is on processing')
    i1 = i0
    for num in range(len(positions)):
        str_po = str(positions[num]) 
        #  E:\\0-PhD\\1 nozzle\\different swirl number\\postprocessing\\z-28.5\\28.5-0.1\\velocity-cut.tiff
        photo_name = v + '-' + photos + '-' + str_po + '.tif'
        photo_position = dir + '\\' + photo_name
        print(photo_position)
        # 插入图片
        image = PPTPres.Slides[i1].Shapes.AddPicture(FileName=photo_position, LinkToFile=False,
                                                    SaveWithDocument=True, Left=x_position, Top=y_position,
                                                    Width=ph_width/unit_point, Height=ph_height/unit_point)
        # 换页
        i1 += 1
    x_position += ph_line/unit_point
    # 图片换行
    if (v_num+1) % j0 == 0:
        x_position = 0
        y_position += ph_col/unit_point
input("all done, press enter to exit")