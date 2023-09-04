import cv2

# 두 개의 이미지 로드
foreground_path = "./Gmail/ori.png"
background_path = "./Gmail/maple1.png"

foreground = cv2.imread(foreground_path)
background = cv2.imread(background_path)



# 이미지 크기를 동일하게 조정 (필요한 경우)
foreground = cv2.resize(foreground, (background.shape[1], background.shape[0]))
foreground = cv2.cvtColor(foreground, cv2.COLOR_BGR2RGB)

# 이미지 합성
composite_image = cv2.add(background, foreground)
composite_image_rgb = cv2.cvtColor(composite_image, cv2.COLOR_BGR2RGB)

# 합성된 이미지를 저장하거나 표시
output_path = "composite_image.jpg"
cv2.imwrite(output_path, composite_image_rgb)

cv2.imshow("Composite Image", composite_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
