import cv2
import numpy as np

cap = cv2.VideoCapture(0)
backgd = cv2.imread('./image.jpg')

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #cv2.imshow('filter', hsv)
        blue = np.uint8([[[0,0,255]]])
        hsv_blue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
        #print(hsv_blue)
        #refer the hsv chart for desired colour
        l_blue = np.array([0,50,50])
        u_blue = np.array([30,255,255])

        mask = cv2.inRange(hsv,l_blue,u_blue)
        #cv2.imshow('mask',mask)

        part1 = cv2.bitwise_and(backgd,backgd,mask = mask)
        #cv2.imshow("part1", part1)

        mask = cv2.bitwise_not(mask)

        part2 = cv2.bitwise_and(frame,frame,mask=mask)
        #kernel = np.ones((2,2), np.uint8)
        #dilation = cv2.dilate(part1+part2,kernel,iterations = 1)
        cv2.imshow("cloak", part1+part2)

    if cv2.waitKey(5) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()