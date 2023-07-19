'''
https://docs.python.org/ko/3/reference
'''


def main():
    score_file = open("score.txt", "r", encoding="utf8")

    lines = score_file.readlines()  # 파일에 있는 모든 줄을 읽어와서 list로 return

    for line in lines:  # lines에 내용이 있는 동안 반복
        print(line, end="")  # 읽어 온 내용 출력

    score_file.close()  # 파일 객체 닫기(자원 반납)


    '''
    점심 : 닭곰탕
    음료 : 아바라
    과학: 80
    코딩: 100
    '''

main()
