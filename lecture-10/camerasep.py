import cv2

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if ret:

        cv2.imshow("my camera", frame)

    key = cv2.waitKey(10)

    if key == ord("q"):
        break
    
    if key == ord("c"):
        cv2.imwrite("myimg.png", frame)
