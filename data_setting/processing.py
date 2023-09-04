import cv2
import os
import noise
import numpy as np

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
    base_filename = f"{last_file_number:03d}"
    original_output_path = os.path.join(output_folder, f"{base_filename}_original.jpg")
    gaussian_blur_output_path = os.path.join(output_folder, f"{base_filename}_gaussian_blur.jpg")
    perlin_noise_output_path = os.path.join(output_folder, f"{base_filename}_perlin_noise.jpg")

    # 이미지 불러오기
    img = cv2.imread(input_path)

    if img is not None:
        # 이미지 복사 (원본 이미지)
        original_img = img.copy()
        cv2.imwrite(original_output_path, original_img)
        
        # 가우시안 블러 적용
        blurred_img = cv2.GaussianBlur(img, (15, 15), 5)
        cv2.imwrite(gaussian_blur_output_path, blurred_img)

        # 이미지 크기 가져오기
        height, width, _ = img.shape

        # 퍼린 노이즈 생성 (모든 값을 255로 설정하여 흰색으로 만듦)
        scale = 100  # 노이즈의 크기 조절
        world = np.ones((height, width), dtype=np.uint8) * 255
        
        # 구름 이미지 생성 (흰색으로 설정)
        clouds_image = np.zeros((height, width, 3), dtype=np.uint8)
        clouds_image[..., 0] = world  # 빨간색 채널에 노이즈 값을 할당
        clouds_image[..., 1] = world  # 녹색 채널에 노이즈 값을 할당
        clouds_image[..., 2] = world  # 블루 채널에 노이즈 값을 할당

        # 퍼린 노이즈 이미지를 원본 이미지와 합성
        perlin_noise_img = cv2.addWeighted(img, 0.7, clouds_image, 0.3, 0)
        cv2.imwrite(perlin_noise_output_path, perlin_noise_img)

        print(f"Processed images saved: {original_output_path}, {gaussian_blur_output_path}, {perlin_noise_output_path}")
    else:
        print(f"Failed to load image: {input_path}")
