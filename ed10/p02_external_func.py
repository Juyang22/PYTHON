import glob


def main():
    print(glob.glob("*.py"))  # 현재 디렉토리에 있는 확장자가 py인 파일 출력
    # ['p01_internal_func.py', 'p02_external_func.py']


main()
