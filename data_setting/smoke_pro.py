import os
import cv2
import noise
import numpy as np

# 입력 폴더와 출력 폴더 경로 설정
input_folder = 'img'  # 입력 폴더 경로
output_folder = 'img_smoke'  # 출력 폴더 경로

# 출력 폴더가 없으면 생성
os.makedirs(output_folder, exist_ok=True)

# 이미지 파일 목록 가져오기
image_files = os.listdir(input_folder)
image_files = [f for f in image_files if f.endswith('.jpg') or f.endswith('.png')]  # 이미지 파일 필터링

# 이미지 파일 별로 작업 수행
for image_file in image_files:
    # 이미지 로드
    input_image_path = os.path.join(input_folder, image_file)
    image = cv2.imread(input_image_path)

    # 이미지 크기 가져오기
    height, width, _ = image.shape

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

    # 구름 이미지와 원본 이미지를 섞어 구름 필터 효과 생성
    blended_image = cv2.addWeighted(image, 0.7, clouds_image, 0.3, 0)

    # 출력 이미지 저장
    output_image_path = os.path.join(output_folder, image_file)
    cv2.imwrite(output_image_path, blended_image)

print("작업이 완료되었습니다.")
