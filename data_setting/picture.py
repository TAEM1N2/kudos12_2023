import cv2
import os

# 웹캠 캡처 객체 생성
cap = cv2.VideoCapture(4)

# 웹캠 오류 처리
if not cap.isOpened():
    print("WebCam is not running")
    exit()

# 이미지 저장 폴더 생성
output_folder = "img"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 이미지 파일 목록 가져오기
existing_files = os.listdir(output_folder)
frame_count = 0

# 기존 파일 중 가장 큰 번호 찾기
if existing_files:
    existing_files.sort()
    last_file = existing_files[-1]
    frame_count = int(last_file.split('.')[0])

while cap.isOpened():
    # 프레임 캡쳐
    ret, frame = cap.read()

    # 프레임을 화면에 표시
    cv2.imshow("Webcam Capture", frame)

    # 1초마다 프레임을 표시하도록 설정
    if cv2.waitKey(1000) & 0xFF == ord('q'):
        break

    # 프레임을 이미지 파일로 저장
    frame_count += 1
    save_file_name = os.path.join(output_folder, f"{frame_count:03d}.jpg")
    cv2.imwrite(save_file_name, frame)

    # 저장된 파일 이름 출력
    print(f"Saved: {save_file_name}")
    
# 사용한 리소스 해제
cap.release()
cv2.destroyAllWindows()
