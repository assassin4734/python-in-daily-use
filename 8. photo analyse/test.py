import numpy as np
import cv2


def cornerdetected(image, opt=1):
    # Detecting corners
    # 可以使用opencv中cv2.cvtColor()函数来改变图像的颜色空间，该函数形式为：cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, mask_all = cv2.threshold(src=gray,             # 要二值化的图片
                       thresh=100,           # 全局阈值
                       maxval=0,           # 大于全局阈值后设定的值
                       type=cv2.THRESH_TOZERO)# 设定的二值化类型，
    cv2.imshow('', gray)
    """
    src单通道输入图像,八位或者浮点数。
    maxCorners表示最大返回关键点数目。
    qualityLevel表示拒绝的关键点 R < qualityLevel x max response将会被直接丢弃。
    minDistance 表示两个关键点之间的最短距离。
    mask 表示mask区域,如果有表明只对mask区域做计算。
    blockSize 计算梯度与微分的窗口区域。
    useHarrisDetector 表示是否使用harris角点检测,默认是false 为shi-tomas。
    k = 0.04默认值,当useHarrisDetector为ture时候起作用。
    """
    corners = cv2.goodFeaturesToTrack(gray, 6, 0.1, 10)
    print(len(corners))
    for pt in corners:
        print(pt)
        # 介于低和高之间的 np.int_ 类型的随机整数
        b = np.random.random_integers(0, 256)
        g = np.random.random_integers(0, 256)
        r = np.random.random_integers(0, 256)
        x = np.int32(pt[0][0])
        y = np.int32(pt[0][1])
        cv2.circle(image, (x, y), 5, (int(b), int(g), int(r)), 2)
    # output
    return image


# 函数imread()返回图像为一个标准的Numpy数组
src = cv2.imread("E:\\1-python-in-daily-use\\8. photo analyse\\15-crosspoint.png")
cv2.imshow("input", src)
result = cornerdetected(src)
cv2.imshow('result', result)
cv2.imwrite("E:\\1-python-in-daily-use\\8. photo analyse\\15-crosspoint-result.png",result)
cv2.waitKey(0)
cv2.destroyAllWindows()