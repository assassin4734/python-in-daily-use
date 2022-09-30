# -encoding utf-8-

'''
1. 将数值模拟得到的图片插入PPT中
2. 按图片类型插入到PPT的不同页上
3. 处理的是变当量比模化算例
'''


from pptx import Presentation, util


# 实例化一个ppt演示文稿
prs = Presentation("数值模拟处理.pptx")
eq_folder = ["eq=0.55", "eq=0.65", "eq=0.75", "eq=0.85", "eq=0.95"]
scale_factor = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
photos = input("请输入图片名称（带扩展名）")
# 定义图片大小（也通过它来定义位置）
ph_width = 3.17
ph_height = 3.74
#定义PPT的页数
i = int(input("请输入PPT的起始页码（0为首张）"))
# 定义换行图片数
j = int(input("请输入换行图片数（整数）"))
# 横向的起始位置, 放在file_folder的循环里就是另一页开始
x_position = 9.51
# 纵向的起始位置, 放在file_folder的循环里就是另一页开始
y_position = 0
for folders in eq_folder:
# 获取目录
    str_folders = str(folders)
    dir_colletion = 'F:\\PhD\\1 nozzle\\re\\postprocessing\\z-' + str_folders
    print(str_folders + ' is on processing')
# 定位PPT
    slide = prs.slides[i]
    # 是否另起slide插入
    # i += 1
# 定义二级目录
    for num in range(len(scale_factor)):
        factors = scale_factor[num]
        str_factors = str(factors)  
        dir_position = 'F:\\PhD\\1 nozzle\\re\\postprocessing\\z-' + str_folders + '\\' + str_folders + '-' + str_factors
        print(str_folders + '-' + str_factors + ' is on going')
# 找到想插入的图片
        photo_position = dir_position + '\\' + photos
        print(photo_position)
        image = slide.shapes.add_picture(
        image_file=photo_position,
        left=util.Cm(x_position),
        top=util.Cm(y_position),
        width=util.Cm(ph_width),
        height=util.Cm(ph_height)
        )
        x_position += ph_width
# 图片换行
        if (num+1) % j == 0:
            x_position = 9.51
            y_position += ph_height
prs.save("F:\\PhD\\1 nozzle\\数值模拟处理-改图.pptx")
print("all done")