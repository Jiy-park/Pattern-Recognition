import numpy as np, cv2

image1 = cv2.imread("images/abs_test1.jpg", cv2.IMREAD_GRAYSCALE) # 명암도 영상 읽기
image2 = cv2.imread("images/abs_test2.jpg", cv2.IMREAD_GRAYSCALE)
if image1 is None or image2 is None: raise Exception("영상 파일 읽기 오류 발생")



x, y, w, h = 100, 100, 7, 3
print("[dif_img1(roi) uint8] = \n%s\n" % dif_img1[y:y+h, x:x+w])
print("[dif_img2(roi) int16]  = \n%s\n"  % dif_img2[y:y+h, x:x+w])
print("[abs_dif1(roi)] = \n%s\n" % abs_dif1[y:y+h, x:x+w])
print("[abs_dif2(roi)] = \n%s\n" % abs_dif2[y:y+h, x:x+w])

titles = ['image1', 'image2', 'dif_img1', 'abs_dif1','abs_dif2']
for title in titles:
    cv2.imshow(title, eval(title))
cv2.waitKey(0)
