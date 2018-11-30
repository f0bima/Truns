# Color Detection

> **TRUNS**

    cv2.findContours(masking, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    cv2.drawContours(frame, contours, -1, warna, thickness)

    M = cv2.moments(contours[0])
    x = int(M['m10'] / M['m00'])
    y = int(M['m01'] / M['m00'])

    cv2.putText(frame, "TEXT", (Coordinate), Font, Size, Warna, thickness)
    
> **BLUE**

    lower = np.array([110, 50, 50])
    upper = np.array([130, 255, 255])
    
> **RED**

    lower = np.array([0, 100, 100])
    upper = np.array([10, 255, 255])
