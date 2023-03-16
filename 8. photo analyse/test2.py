import numpy as np
import cv2 as cv


def process(image, opt=1):
    # Detecting corners
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    corners = cv.goodFeaturesToTrack(gray, 5, 0.1, 10)
    print(len(corners))
    for pt in corners:
        print(pt)
        b = np.random.random_integers(0, 256)
        g = np.random.random_integers(0, 256)
        r = np.random.random_integers(0, 256)
        x = np.int32(pt[0][0])
        y = np.int32(pt[0][1])
        cv.circle(image, (x, y), 5, (int(b), int(g), int(r)), 2)

    # detect sub-pixel
    winSize = (3, 3)
    zeroZone = (-1, -1)

    # Stop condition
    criteria = (cv.TERM_CRITERIA_EPS + cv.TermCriteria_COUNT, 40, 0.001)
    # Calculate the refined corner locations
    corners = cv.cornerSubPix(gray, corners, winSize, zeroZone, criteria)
    # display
    for i in range(corners.shape[0]):
        print(" -- Refined Corner [", i, "]  (", corners[i, 0, 0], ",", corners[i, 0, 1], ")")
    return image

src = cv.imread("E:\\1-python-in-daily-use\\8. photo analyse\\15-crosspoint.png")
cv.imshow("input", src)
result = process(src)
cv.imshow('result', result)
cv.imwrite('E:\\1-python-in-daily-use\\8. photo analyse\\15-crosspoint-result.png',result)
cv.waitKey(0)
cv.destroyAllWindows()

