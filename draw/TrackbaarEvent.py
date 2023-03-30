import numpy as np
import cv2

def onChange(val):
    global image, title

    add_val = val - int(image[0][0])
    print("추가 화소값:", add_val)
    image = image + add_val
    cv2.imshow(title, image)

image = np.zeros((300, 500), np.uint8)
title = "Trackbar Event"

cv2.imshow(title, image)

cv2.createTrackbar("Brightness", title, image[0][0], 255, onChange)
cv2.waitKey(0)
cv2.destroyAllWindows()