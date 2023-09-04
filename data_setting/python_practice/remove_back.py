import cv2
import numpy as np

# 객체 이미지와 배경 이미지 로드
object_image = cv2.imread('./img/001.jpg')
background_image = cv2.imread('./img/032.jpg')

# 객체 이미지를 그레이스케일로 변환
gray_object = cv2.cvtColor(object_image, cv2.COLOR_BGR2GRAY)

# 무작위로 배경과 객체를 구분하기 위한 임계값 처리
_, mask = cv2.threshold(gray_object, 1, 255, cv2.THRESH_BINARY)

# 배경과 객체의 경계선 부분의 마스크 생성
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contour_mask = np.zeros_like(mask)
cv2.drawContours(contour_mask, contours, -1, 255, thickness=cv2.FILLED)

# 마스크 이미지 저장
cv2.imwrite('mask_image.png', contour_mask)

# 배경 이미지 로드
new_background_image = cv2.imread('./img/023.jpg')

# 마스크 이미지 로드
mask = cv2.imread('mask_image.png', 0)

# 객체 크기에 맞춰 배경 이미지 리사이즈
new_background_image = cv2.resize(new_background_image, (object_image.shape[1], object_image.shape[0]))

# 배경 합성
final_image = cv2.bitwise_and(object_image, object_image, mask=255 - mask)
background = cv2.bitwise_and(new_background_image, new_background_image, mask=mask)
composite_image = cv2.add(final_image, background)

# 결과 이미지 출력
cv2.imshow('Composite Image', composite_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
