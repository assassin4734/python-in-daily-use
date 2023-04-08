import win32com.client as client


def input_function():
    act_str = input("请输入图片名称:\n0: 无量纲轴向速度\n1: 无量纲径向速度\n")
    if act_str == "0":
        photo_name = '无量纲轴向速度'
        return(photo_name)
    elif act_str == "1":
        photo_name = '无量纲径向速度'
        return(photo_name)
    else:
        print("input error!")
        input_function()


def val_function():
    act_str = input("请输入变量名称:\n0: 变旋流数\n1: 变当量比")
    if act_str == "0":
        val_name = '变旋流数'
        return(val_name)
    elif act_str == "1":
        val_name = '变当量比'
        return(val_name)
    else:
        print("input error!")
        val_function()


# 实例化一个ppt演示文稿
PPT = client.GetActiveObject("Powerpoint.Application")
PPTPres = PPT.ActivePresentation
print("共有" + str(len(PPTPres.Slides)) + "张slide")
print('# 定义磅值与厘米的换算基准')
unit_point = 0.03527
print('# 定义图片类型')
data = input_function()
print('# 定义图片大小（也通过它来定义位置）')
print('图片宽度是3厘米')
ph_width = float(input('输入图片宽度：'))
print('图片高度是2.91厘米')
ph_height = float(input('输入图片高度：'))
print('横向间距是3厘米')
ph_line = float(input('输入横向间距:'))
print('纵向间距是2.91厘米')
ph_col = float(input('输入纵向间距:'))
print('# 定义PPT的页数')
i0 = int(input("请输入PPT的起始页码（0为首张）"))
print('# 定义种类')
variable = val_function()
print('# 横向的起始位置')
x_position = 0.4/unit_point
print('# 纵向的起始位置')
y_position = 0.8/unit_point
print('定位后处理的目录')
onenozzlefolder = {'变当量比': 'eq\\postprocessing-transport\\',
                   '变旋流数': 'different swirl number\\postprocessing\\'}
folder = {'sw_folder': ["z-28.5", "z-35.5", "z-40.5", "z-45.5", "z-52.5"],
          'eq_folder': ["eq=0.55", "eq=0.65", "eq=0.75", "eq=0.85", "eq=0.95"]}
positions = [1, 2, 3, 4]
dir = 'E:\\0-PhD\\1 nozzle\\'
if variable == '变当量比':
    fol = 'eq_folder'
elif variable == '变旋流数':
    fol = 'sw_folder'
else:
    pass
dir_para = dir + onenozzlefolder[variable]
print(dir_para + '正被处理')
for var in folder[fol]:
    dir_origin = dir_para + var + '\\'
    dir_graph = dir_origin + var + '-' + data
    for pos in positions:
        i1 = i0
        dir_pos = dir_graph + '-' + str(pos) + '-cut.png'
        print(dir_pos)
        image = PPTPres.Slides[i1].Shapes.AddPicture(FileName=dir_pos, LinkToFile=False,
                                            SaveWithDocument=True, Left=x_position, Top=y_position,
                                            Width=ph_width/unit_point, Height=ph_height/unit_point)
        y_position += ph_col/unit_point
    x_position += ph_line/unit_point
    y_position = 0.8/unit_point
input('all done')