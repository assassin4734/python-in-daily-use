from PIL import Image, ImageDraw
# PIL有九种不同模式: 1，L，P，RGB，RGBA，CMYK，YCbCr，I，F。大家可以尝试每一种
# 1：表示将彩图为二值图像，非黑即白。每个像素用8个bit表示，0表示黑，255表示白。
# L:表示将彩色图片转换为灰度图像，每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。
# 转换公式：L = R * 299/1000 + G * 587/1000+ B * 114/1000。
# P: 8位像素，使用调色板映射到任何其他模式，具体的功能可以区官网查看，或者自己尝试使用，但不经常使用
# RGB: 通常是对彩色图片进行加强3x8位像素，真彩色
# RGBA: 4x8位像素，带透明度掩模的真彩色
# CMYK: 4x8位像素，分色
# YCbCr: 3x8位像素，彩色视频格式
# I: 32位有符号整数像素
# F: 32位浮点像素


s_n = []
e_n = []
image_e = r'E:\0-PhD\1 nozzle\论文\POF\Study...Numbers-manuscripts and related files\审稿意见\试验与计算对比\火焰-试验.png'
image_s = r'E:\0-PhD\1 nozzle\论文\POF\Study...Numbers-manuscripts and related files\审稿意见\试验与计算对比\火焰-计算.png'
# 处理计算
load_image1 = Image.open(image_s)
width1, height1 = load_image1.size
print('Image size: {}x{}'.format(width1, height1))
convert_image1 = load_image1.convert('L')
# draw = ImageDraw.Draw(convert_image1)
# draw.point((300, 300), fill="red")
# X,Y = 300, 800
# r = 5
# draw.ellipse([(X-r,Y-r),(X+r,Y+r)], fill = 'red',outline ='red')
convert_image1.show()
X = 300
Y = 100
while Y < 801:
    gray_value1 = convert_image1.getpixel((X, Y))
    s_n.append(gray_value1)
    Y += 7
# with open(r'E:\0-PhD\1 nozzle\论文\POF\Study...Numbers-manuscripts and related files\审稿意见\试验与计算对比\计算.txt', 'w') as f:
#     f.write(','.join(s_n))
# f.close()
print(s_n)
# 处理试验
load_image2 = Image.open(image_e)
width2, height2 = load_image2.size
print('Image size: {}x{}'.format(width2, height2))
convert_image2 = load_image2.convert('L')
convert_image2.show()
X = 300
Y = 100
while Y < 801:
    gray_value2 = convert_image2.getpixel((X, Y))
    e_n.append(gray_value2)
    Y += 7
print(e_n)