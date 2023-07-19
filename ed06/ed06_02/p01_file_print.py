'''
https://docs.python.org/ko/3/reference
'''


def main():
    score_file = open("score.txt", "w", encoding="utf8")
    print("점심 : 닭곰탕", file=score_file)  # score.txt 파일에 내용 쓰기
    print("음료 : 아바라", file=score_file)
    # 로그 남기는 데 이용 가능

    score_file.close()  # score.txt 닫기

main()

'''
    점심 : 닭곰탕
    음료 : 아바라
'''