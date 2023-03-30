import cv2
import numpy as np

image = cv2.imread("image/flip_test.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상 파일 읽기 오류 발생") # 예외 처리

if image.dtype == 'uint8':     mat_type = "CV_8U"
elif image.dtype == 'int8':    mat_type = "CV_8S"
elif image.dtype == 'uint16':  mat_type = "CV_16U"
elif image.dtype == 'int16':   mat_type = "CV_16S"
elif image.dtype == 'float32': mat_type = "CV_32F"
elif image.dtype == 'float64': mat_type = "CV_64F"

image_copy = np.zeros((image.shape[0],image.shape[1],image.shape[2]), image.dtype)


for i in range(image.shape[0]):#가로 반복문
   for j in range(image.shape[1]):#세로 반복문
      #각 채널 복사
       image_copy[i][j][0] = image[i][j][0]
       image_copy[i][j][1] = image[i][j][1]
       image_copy[i][j][2] = image[i][j][2]


x_axis=np.zeros((image.shape[0],image.shape[1],image.shape[2]), image.dtype)
for i in range(image.shape[0]):
   for j in range(image.shape[1]):
      #각 채널 복사
       x_axis[image.shape[0]-1-i][j][0] = image[i][j][0]
       x_axis[image.shape[0]-1-i][j][1] = image[i][j][1]
       x_axis[image.shape[0]-1-i][j][2] = image[i][j][2]

y_axis=np.zeros((image.shape[0],image.shape[1],image.shape[2]), image.dtype)
for i in range(image.shape[0]):
   for j in range(image.shape[1]):
      #각 채널 복사
      y_axis[i][image.shape[1] - 1 - j][0] = image[i][j][0]
      y_axis[i][image.shape[1] - 1 - j][1] = image[i][j][1]
      y_axis[i][image.shape[1] - 1 - j][2] = image[i][j][2]

#                                     가로를 두배로 늘림.
rep_image=np.zeros((image.shape[0],image.shape[1]*2,image.shape[2]), image.dtype)
for i in range(image.shape[0]):
   for j in range(image.shape[1]):
      #각 채널 복사
      rep_image[i][j + image.shape[1]][0] = image[i][j][0]
      rep_image[i][j + image.shape[1]][1] = image[i][j][1]
      rep_image[i][j + image.shape[1]][2] = image[i][j][2]
      rep_image[i][j][0] = image[i][j][0]
      rep_image[i][j][1] = image[i][j][1]
      rep_image[i][j][2] = image[i][j][2]

#좌우반전
xy_axis=np.zeros((image.shape[0],image.shape[1],image.shape[2]), image.dtype)
for i in range(image.shape[0]):  # 세로 반복문
    for j in range(image.shape[1]):  # 가로 반복문
        # 각 채널 복사
        xy_axis[image.shape[0]-1-i][image.shape[1]-1-j][0] = image[i][j][0]
        xy_axis[image.shape[0]-1-i][image.shape[1]-1-j][1] = image[i][j][1]
        xy_axis[image.shape[0]-1-i][image.shape[1]-1-j][2] = image[i][j][2]

#m*n이 m*n으로 바뀌는 행렬전치.
trans_image = np.zeros((image.shape[1], image.shape[0], image.shape[2]), image.dtype)

for i in range(image.shape[0]):  # 세로 반복문
    for j in range(image.shape[1]):  # 가로 반복문
        # 각 채널 복사
        trans_image[j][i][0] = image[i][j][0]
        trans_image[j][i][1] = image[i][j][1]
        trans_image[j][i][2] = image[i][j][2]

## 각 행렬을 영상으로 표시
titles = ['image', 'x_axis', 'y_axis','xy_axis','rep_image','trans_image']
for title in titles:
    cv2.imshow(title, eval(title))
cv2.waitKey(0)