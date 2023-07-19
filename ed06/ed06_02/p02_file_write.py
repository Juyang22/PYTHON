'''
https://docs.python.org/ko/3/reference
'''

# write()로 파일에 내용 쓰기
def main():
    score_file = open("score.txt", "a", encoding="utf8")

    score_file.write("과학: 80\n")
    score_file.write("코딩: 100\n")

    score_file.close()  # 닫기

main()

'''
    점심 : 닭곰탕
    음료 : 아바라
    과학: 80
    코딩: 100
'''
