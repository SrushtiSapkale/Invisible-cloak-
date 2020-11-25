import cv2
capture = cv2.VideoCapture(0)

while capture.isOpened():
    ret, backgd = capture.read()
    if ret:
        cv2.imshow("image", backgd)
    if cv2.waitKey(5) == ord('q'):
            cv2.imwrite('image.jpg', backgd)
            break

capture.release()
cv2.destroyAllWindows()


