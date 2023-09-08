import os
import random
import shutil

# 원본 데이터가 있는 디렉토리 경로
data_dir = '/home/tae/dev_ws/yolov5/coco/lab'

# 분할된 데이터를 저장할 디렉토리 경로
train_dir = '/home/tae/dev_ws/yolov5/dataset/lables/train'
val_dir = '/home/tae/dev_ws/yolov5/dataset/lables/val'
test_dir = '//home/tae/dev_ws/yolov5/dataset/lables/test'

# 분할 비율
train_ratio = 0.7
val_ratio = 0.1
test_ratio = 0.1

# 디렉토리 생성
os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# 데이터 파일 목록 가져오기
data_files = os.listdir(data_dir)

# 데이터를 무작위로 섞음
random.shuffle(data_files)

# 데이터를 분할해서 복사
total_count = len(data_files)
train_count = int(total_count * train_ratio)
val_count = int(total_count * val_ratio)

train_files = data_files[:train_count]
val_files = data_files[train_count:train_count+val_count]
test_files = data_files[train_count+val_count:]

# 분할된 파일들을 복사
for filename in train_files:
    src_path = os.path.join(data_dir, filename)
    dst_path = os.path.join(train_dir, filename)
    shutil.copy(src_path, dst_path)

for filename in val_files:
    src_path = os.path.join(data_dir, filename)
    dst_path = os.path.join(val_dir, filename)
    shutil.copy(src_path, dst_path)

for filename in test_files:
    src_path = os.path.join(data_dir, filename)
    dst_path = os.path.join(test_dir, filename)
    shutil.copy(src_path, dst_path)

print("데이터 분할이 완료되었습니다.")
