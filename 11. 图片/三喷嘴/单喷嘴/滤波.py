import cv2

img = cv2.imread('E:\\0-PhD\\1 nozzle\\z-experiment\\z-reaction state\\5us000000050.bmp')
gaussian = cv2.GaussianBlur(img, (5,5), 0)
cv2.imshow('Gaussian filter', gaussian)
cv2.waitKey(0)
cv2.destroyAllWindows()

# # 导入库
# from PIL import Image
# # 加载原始图像
# image = Image.open('E:\\0-PhD\\1 nozzle\\z-experiment\\z-reaction state\\5us000000050.bmp')
# # 将图像转化为灰度图像
# gray_image = image.convert('L')
# # 设置二值化阈值，取值范围为0-255
# threshold = 100
# # 将灰度图像二值化
# binary_image = gray_image.point(lambda x: 255 if x > threshold else 0, '1')
# # 保存二值化后的图像
# binary_image.save('E:\\0-PhD\\1 nozzle\\z-experiment\\z-reaction state\\test.bmp')