import os
import shutil

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def move_files(source_dir, dest_dir, extensions):
    create_directory(dest_dir)
    for filename in os.listdir(source_dir):
        if any(filename.lower().endswith(ext) for ext in extensions):
            source_path = os.path.join(source_dir, filename)
            dest_path = os.path.join(dest_dir, filename)
            shutil.move(source_path, dest_path)

def main():
    download_dir = r'C:\Users\student\Downloads'
    
    # 각 카테고리별로 이동할 폴더 지정
    image_dir = os.path.join(download_dir, 'images')
    data_dir = os.path.join(download_dir, 'data')
    docs_dir = os.path.join(download_dir, 'docs')
    archive_dir = os.path.join(download_dir, 'archive')
    
    # 파일 유형별로 이동할 확장자 목록
    image_extensions = ['.jpg', '.jpeg']
    data_extensions = ['.csv', '.xlsx']
    docs_extensions = ['.txt', '.doc', '.pdf']
    archive_extensions = ['.zip']
    
    # 파일 이동
    move_files(download_dir, image_dir, image_extensions)
    move_files(download_dir, data_dir, data_extensions)
    move_files(download_dir, docs_dir, docs_extensions)
    move_files(download_dir, archive_dir, archive_extensions)

if __name__ == "__main__":
    main()
