import cv2
import os

# 원본 이미지 폴더 경로
input_folder = "img"

# 결과 이미지 폴더 경로
output_folder = "img_fog"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 원본 이미지 파일 목록 가져오기
image_files = sorted([f for f in os.listdir(input_folder) if f.endswith(".jpg")])

for image_file in image_files:
    
    # 이미지 파일 경로 설정
    input_path = os.path.join(input_folder, image_file)
    output_path = os.path.join(output_folder, image_file)

    # 이미지 불러오기
    img = cv2.imread(input_path)

    if img is not None:
        # 가우시안 블러 적용
        blurred_img = cv2.GaussianBlur(img, (15, 15), 5)

        # 결과 이미지 저장
        cv2.imwrite(output_path, blurred_img)
        print(f"Processed image saved: {output_path}")
    else:
        print(f"Failed to load image: {input_path}")
