import cv2
import numpy as np
import os

# 读取图像
lin = os.listdir('D:\\linlin\\')
for li in lin:
    img = cv2.imread('D:\\linlin\\'+li)
    # 将图像转换为HSV颜色空间
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # 定义红色在HSV颜色空间中的取值范围，以及二值化阈值
    lower_red = np.array([0, 50, 50])
    upper_red = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    lower_red = np.array([170, 50, 50])
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)
    # 结合两个面具
    mask = cv2.bitwise_or(mask1, mask2)
    # 将二值化结果应用于原始图像，并将红色像素设置为白色，将非红色像素设置黑色
    result = np.zeros_like(img)
    result[mask == 255] = [0, 0, 0]  # 将红色像素设置为黑色
    result[mask != 255] = [255, 255, 255]  # 将非红色像素设置为白色
    xy = np.column_stack(np.where(result==0))
    print(xy)
    for c in xy:
        print(c)
        changefile = cv2.circle(img=img, center=(int(c[1]), int(c[0])), radius=2, color=(255, 255, 255),thickness=5)
    cv2.imwrite('D:\\linlin\\'+li.strip('png')+'-change.png', changefile)
print('all done')
# # 保存结果图像
# cv2.imwrite('D:\\linlin\\test.png', result)

# # 显示结果图像
# cv2.imshow('Result', result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

