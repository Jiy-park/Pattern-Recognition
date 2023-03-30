import cv2
import numpy as np

image = cv2.imread("image/flip_test.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상 파일 읽기 오류 발생") # 예외 처리

#image.shape[0] : 1차원 배열의 길이
#image.shape[1] : 2차원 배열의 길이
#image.shape[2] : 3차원 배열의 길이
#image.dtype : 현재 배열의 데이터 타입

#image_copy = np.zeros((  ,  , ), image.dtype)
#for 가로 반복문  
#    for 세로 반복문
#       각 채널 복사  
#        image_copy[i][j][0] = image[i][j][0]
#        image_copy[i][j][1] = image[i][j][1]
#        image_copy[i][j][2] = image[i][j][2]


## 각 행렬을 영상으로 표시
titles = ['image', 'image_copy','x_axis', 'y_axis','xy_axis','rep_image','trans_image']
for title in titles:
    cv2.imshow(title, eval(title))
cv2.waitKey(0)