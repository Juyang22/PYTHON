'''
https://docs.python.org/ko/3/reference
'''

import os


def main():
    # ['2023', 'p01_internal_func.py', 'p02_external_func.py', 'p03_os.py', 'p04_mkdirs.py', 'p05_rmdir.py', 'p06_file_list.py']
    print(os.listdir())  # 현재 디렉토리 내의 폴더 및 파일 목록 출력


main()
