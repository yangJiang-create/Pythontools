import cv2

def click_info(event, x, y, flags, param):
    # 只处理双击事件
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print('坐标', x, y)
        b, g, r = img[y, x]     # 获取b, g, r
        print("像素点的bgr值", b, g, r)

cv2.namedWindow('image')
cv2.setMouseCallback('image',  click_info)

img = cv2.imread('52ef2fecca3bfe069def06acccfe654 (1).png')
while True:
    cv2.imshow("image", img)
    # 点击 esc键
    if cv2.waitKey(20) & 0xFF ==27:
        break

cv2.destroyAllWindows()

'''
先双击，获取你要计算的颜色的RGB值
像素点的bgr值 0 128 0--->绿色
像素点的bgr值 191 191 191--->白色
像素点的bgr值 38 4 145--->红色
'''