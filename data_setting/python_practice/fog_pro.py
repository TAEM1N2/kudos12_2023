import cv2
import os

# 원본 이미지 폴더 경로
input_folder = "img (copy)"

# 결과 이미지 폴더 경로
output_folder = "img"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 원본 이미지 파일 목록 가져오기
image_files = sorted([f for f in os.listdir(input_folder) if f.endswith(".jpg")])

# 이미지 파일 중 가장 큰 번호 찾기
if image_files:
    image_files.sort()
    last_file = image_files[-1]
    last_file_number = int(last_file.split('.')[0])
else:
    last_file_number = 0

for image_file in image_files:
    # 이미지 파일 경로 설정
    input_path = os.path.join(input_folder, image_file)
    
    # 이미지 파일 번호 증가
    last_file_number += 1
    
    # 새로운 파일 이름 생성
    new_image_file = f"{last_file_number:03d}.jpg"
    output_path = os.path.join(output_folder, new_image_file)

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
