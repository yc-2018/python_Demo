import cv2
cap = cv2.VideoCapture(0)
while True:
    # 捕获图像
    ret, frame = cap.read()
    # 显示图像
    cv2.imshow('Video', frame)
    # 按下q键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# 释放资源
cap.release()
cv2.destroyAllWindows()

