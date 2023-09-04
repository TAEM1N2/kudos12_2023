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
    new_image_file = f"{last_file_number:03d}.jpg"
    output_path = os.path.join(output_folder, new_image_file)

    # 이미지 불러오기
    img = cv2.imread(input_path)

    if img is not None:
        # 이미지 크기 가져오기
        height, width, _ = img.shape

        # 퍼린 노이즈 생성
        scale = 100  # 노이즈의 크기 조절
        world = np.zeros((height, width))
        for y in range(height):
            for x in range(width):
                world[y, x] = noise.pnoise2(x/scale, y/scale, octaves=6, persistence=0.5, lacunarity=2.0)

        # 노이즈 값을 0~255 범위로 매핑
        noise_min = np.min(world)
        noise_max = np.max(world)
        world = (world - noise_min) / (noise_max - noise_min) * 255

        # 구름 이미지 생성
        clouds_image = np.zeros((height, width, 3), dtype=np.uint8)
        clouds_image[..., 0] = world  # 빨간색 채널에 노이즈 값을 할당
        clouds_image[..., 1] = world  # 녹색 채널에 노이즈 값을 할당
        clouds_image[..., 2] = world  # 블루 채널에 노이즈 값을 할당

        # 퍼린 노이즈 이미지를 원본 이미지와 합성
        blended_img = cv2.addWeighted(img, 0.7, clouds_image, 0.3, 0)

        # 결과 이미지 저장
        cv2.imwrite(output_path, blended_img)
        print(f"Processed image saved: {output_path}")
    else:
        print(f"Failed to load image: {input_path}")
