import os

def rename_images(folder_path):
    # 지정한 폴더 내의 모든 파일 목록 가져오기
    file_list = os.listdir(folder_path)
    
    # 이미지 파일만 골라내기
    image_files = [f for f in file_list if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    
    # 이미지 파일을 순회하며 이름 변경
    for idx, old_name in enumerate(image_files, start=1):
        file_extension = os.path.splitext(old_name)[-1]
        new_name = f"f{idx}{file_extension}"
        
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, new_name)
        
        os.rename(old_path, new_path)
        print(f"Renamed: {old_name} -> {new_name}")

# 이미지 파일이 들어있는 폴더 경로 설정
image_folder_path = "img_fog"

# 이미지 파일 이름 변경 실행
rename_images(image_folder_path)
