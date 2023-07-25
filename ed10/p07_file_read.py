import os


def read_files_in_dir(dir_path):
    # print('dir_path', dir_path)
    # 디렉토리 내 파일 목록 조회
    file_list = os.listdir(dir_path)

    for filename in file_list:
        # 디렉토리 > 파일명
        file_path = os.path.join(dir_path, filename)
        # print(file_path)

        # 디렉토리이면 건너뛰기
        if os.path.isdir(file_path):
            continue
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                print(f'-----------------------{filename}-----------------------')
                print(content)
                print('-' * 50)
        except Exception as e:
            print(f'파일: {filename} 읽기 오류: {str(e)}')


def main():
    read_files_in_dir(os.getcwd())  # 현재 디렉토리 정보 전달


main()
