'''
https://docs.python.org/ko/3/reference
'''


def main():
    score_file = open("score.txt", "r", encoding="utf8")

    while True:
        line = score_file.readline()

        if not line: # 더 이상 읽어올 내용이 없을 때
            break  # 반복문 탈출
        print(line, end="")

    score_file.close()


    '''
    점심 : 닭곰탕
    음료 : 아바라
    과학: 80
    코딩: 100
    '''

main()
