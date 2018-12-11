import cv2
import numpy as np


source = cv2.imread('rgb.jpg')
hsv = cv2.cvtColor(source, cv2.COLOR_BGR2HSV)

lower = np.array([110, 50, 50])
upper = np.array([130, 255, 255])

masking = cv2.inRange(hsv, lower, upper)
bitwise = cv2.bitwise_and(source, source, mask=masking)
_, contours, _ = cv2.findContours(masking, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(source, contours, -1, (0, 0, 255), 3)

area = cv2.contourArea(contours[0])
M = cv2.moments(contours[0])
cx = int(M['m10'] / M['m00'])
cy = int(M['m01'] / M['m00'])

x, y, w, h = cv2.boundingRect(contours[0])

cv2.putText(source, str(cx) + ", " + str(cy), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)


cv2.imshow("Source", source)
cv2.imshow("HSV", hsv)
cv2.imshow("Mask", masking)
cv2.imshow("Bitwise", bitwise)

cv2.waitKey()
