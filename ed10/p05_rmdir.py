import os


def main():
    folder = "2023"

    if os.path.exists(folder):  # 같은 이름의 폴더가 존재하면
        print('이미 폴더가 존재합니다.')
        # 디렉토리 삭제
        os.rmdir(folder)
        print(folder, '폴더가 삭제되었습니다.')
    else:  # 폴더가 없으면
        os.makedirs(folder)
        print(folder, '폴더를 생성했습니다.')

main()
