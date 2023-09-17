import cv2 as cv
import numpy as np


# read the image
img = cv.imread("E:\\0-PhD\\3 nozzle\\experimental data\\flame.png")

# 在HSV中:H是色调,取值为[0-180]。S是饱和度,取值为[0-255]。V是黑色度,取值为[0-255]，黑色是0，白色是255
# convert the BGR image to HSV colour space
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# set the lower and upper bounds for the green hue
lower_blue = np.array([100, 80, 46])
upper_blue = np.array([124, 255, 255])

# create a mask for green colour using inRange function
# 低于下限的值，图像变为0；高于上限的值，图像变为0，在中间的值变为255，最后输出的就是中间的这些值
mask = cv.inRange(hsv, lower_blue, upper_blue)

'''
perform bitwise and on the original image arrays using the mask

这样就不用循环给指定位置像素赋值了，比较方便

cv2.bitwise_and()是对二进制数据进行“与”操作，即对图像（灰度图像或彩色图像均可）每个像素值进行二进制“与”操作，
1&1=1（保留的是第一个参数的值），1&0=0，0&1=0，0&0=0

mask：图像掩膜，可选参数，为8位单通道的灰度图像，用于指定要更改的输出图像数组的元素，
即输出图像像素只有mask对应位置元素不为0的部分才输出，否则该位置像素的所有通道分量都设置为0
'''
res = cv.bitwise_and(img, img, mask=mask)

# create resizable windows for displaying the images
cv.namedWindow("res", cv.WINDOW_NORMAL)
cv.namedWindow("hsv", cv.WINDOW_NORMAL)
cv.namedWindow("mask", cv.WINDOW_NORMAL)

# display the images
cv.imshow("mask", mask)
cv.imshow("hsv", hsv)
cv.imshow("res", res)

if cv.waitKey(0):
    cv.destroyAllWindows()
