'''
https://docs.python.org/ko/3/reference
'''


def main():
    score_file = open("score.txt", "r", encoding="utf8")
    # readline : 한 줄 읽어온 후 다음 줄로 이동
    print(score_file.readline(), end="")  # end 값을 ""로 설정하여 줄바꿈 중복 수행 방지
    print(score_file.readline(), end="")
    print(score_file.readline(), end="")
    print(score_file.readline(), end="")

    score_file.close()

main()
