import numpy as np
import cv2


cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
    ret, thresh_img = cv2.threshold(blur,91,255,cv2.THRESH_BINARY)

    contours =  cv2.findContours(thresh_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2]
    for c in contours:
        cv2.drawContours(frame, [c], -1, (0,0,0),-1)

    for h, cnt in enumerate(contours):
        mask = np.zeros(gray.shape, np.uint8)
        cv2.drawContours(mask, [cnt], 0, 255, -1)
        mean = cv2.mean(frame, mask=mask)

     # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()