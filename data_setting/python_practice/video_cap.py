import cv2
import os

# 비디오 파일 경로 설정
video_path = "차체 영상 1차.mp4"

# 저장할 이미지 파일을 저장할 폴더 경로 설정
output_folder = "video"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 비디오 캡쳐 객체 생성
cap = cv2.VideoCapture(video_path)

# 캡쳐가 올바르게 열렸는지 확인
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# 프레임 캡쳐 설정
frame_count = 0

while True:
    # 프레임 캡쳐
    ret, frame = cap.read()

    # 비디오의 끝에 도달하면 종료
    if not ret:
        break

    # 이미지 파일 경로 설정
    image_path = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")

    # 이미지 파일로 저장
    cv2.imwrite(image_path, frame)

    frame_count += 1

# 사용한 리소스 해제
cap.release()
cv2.destroyAllWindows()

print(f"{frame_count} frames captured and saved to '{output_folder}'")
