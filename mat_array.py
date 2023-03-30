import cv2
import numpy as np

image = cv2.imread("image/flip_test.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상 파일 읽기 오류 발생") # 예외 처리


## 각 행렬을 영상으로 표시
titles = ['image', 'x_axis', 'y_axis', 'xy_axis', 'rep_image', 'trans_image']


rep_image = np.zeros((image.shape[0], image.shape[1]*2, image.shape[2]), image.dtype) # 세로, 가로




for title in titles:
    cv2.imshow(title, rep_image)
cv2.waitKey(0)