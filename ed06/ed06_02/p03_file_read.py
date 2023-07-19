'''
https://docs.python.org/ko/3/reference
'''


def main():
    # score.txt 파일을 읽기 모드로 열기
    # Copy path/Reference -> 경로 복사
    # path 구분자 = '/'
    file_path = "C:/JSPA_0309/04_PYTHON/04_01_PYTHON/workspace/ed06/ed06_02/score.txt"
    score_file = open(file_path, "r", encoding="utf8")

    # 파일 전체 읽기
    print(score_file.read())

    score_file.close()

    '''
    점심 : 닭곰탕
    음료 : 아바라
    과학: 80
    코딩: 100
    '''
main()
