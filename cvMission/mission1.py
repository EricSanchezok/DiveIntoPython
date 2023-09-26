import cv2
import numpy as np

# 题目要求：使用电脑摄像头，使用颜色识别，检测出乒乓球的质心和外接圆，并显示出来。

cap = cv2.VideoCapture(0)

# 鼠标点击显示RGB和HSV值
def getpos(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("HSV:", hsv[y, x])

cv2.namedWindow("frame")
cv2.setMouseCallback("frame", getpos)

upper = np.array([30, 200, 255])
lower = np.array([0, 90, 200])

while True:
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 颜色检测
    mask = cv2.inRange(hsv, lower, upper)
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.erode(mask, kernel, iterations=3)
    mask = cv2.dilate(mask, kernel, iterations=2)

    # 轮廓检测
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        # 找到最大轮廓
        c = max(contours, key=cv2.contourArea)
        if cv2.contourArea(c) > 100:
            # 计算最大轮廓的外接圆
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            # 计算最大轮廓的矩形边界
            rect = cv2.minAreaRect(c)
            # 绘制最大轮廓的外接圆
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            # 绘制最大轮廓的质心
            cv2.circle(frame, (int(rect[0][0]), int(rect[0][1])), 2, (0, 0, 255), 2)

    cv2.imshow("frame", frame)


    key = cv2.waitKey(1)

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()


# 练习：使用电脑摄像头，使用霍夫圆检测，检测出乒乓球的质心和外接圆，并显示出来。