import os
import shutil
# week1 하위의 파일만 모두 test.folder에 복사하시오

# week1 파일 리스트 가져오기
#2. 파일리스트 반복문
# test_folder로 copy
#shutil.copy('원본경로', '저장경로')


root = os.getcwd()
copy_dir = './test_folder'

for nm in os.listdir(root):
    path = os.path.join(root, nm)
    #파일만
    if os.path.isfile(path):
        copy_file_path = os.path.join(copy_dir, nm)
        shutil.copy(path, copy_file_path)
print("복사 완료")
