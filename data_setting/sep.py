import os
import shutil

# 원본 파일들이 위치한 디렉토리 경로
source_folder = '/home/tae/dev_ws/kudos12_2023/data_setting/Yolo_mark/x64/Release/data/img'

# .jpg 파일을 저장할 디렉토리 경로
jpg_output_folder = '/home/tae/dev_ws/yolov5/coco/images'

# .txt 파일을 저장할 디렉토리 경로
txt_output_folder = '//home/tae/dev_ws/yolov5/coco/lables'

# 디렉토리가 존재하지 않으면 생성
os.makedirs(jpg_output_folder, exist_ok=True)
os.makedirs(txt_output_folder, exist_ok=True)

# 원본 디렉토리 내 모든 파일 검색
for filename in os.listdir(source_folder):
    source_file_path = os.path.join(source_folder, filename)
    
    # 파일 확장자 확인
    file_extension = filename.split('.')[-1].lower()
    
    # .jpg 파일인 경우 jpg_output_folder로 복사
    if file_extension == 'png':
        shutil.copy(source_file_path, os.path.join(jpg_output_folder, filename))
    
    # .txt 파일인 경우 txt_output_folder로 복사
    elif file_extension == 'txt':
        shutil.copy(source_file_path, os.path.join(txt_output_folder, filename))

print("분리 및 복사가 완료되었습니다.")
