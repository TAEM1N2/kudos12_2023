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

frame_count = 0

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

# 사용한 리소스 해제
cap.release()
cv2.destroyAllWindows()
