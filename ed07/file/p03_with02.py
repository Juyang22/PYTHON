'''
https://docs.python.org/ko/3/reference
'''


def main():
    # 새로운 study.txt 파일 생성
    with open("study.txt", "w", encoding="utf8") as study_file:
        study_file.write("파이썬 공부 중~!~!")

    # study.txt 파일 읽기
    with open("study.txt", "r", encoding="utf8") as study_file:
        print(study_file.read())  # 파이썬 공부 중~!~!

    # split()
    str01 = "스프링, 파이썬"
    print(str01.split(", "))  # ['스프링', '파이썬'] -> list(배열)

    str02 = "스프링 파이썬"
    print(str02.split())  # default = " " (공백)

    # endswith() : 문자열이 어떤 값으로 끝나는지 확인할 때 사용
    str03 = "이 문장은 마침표로 끝납니다."

    if str03.endswith("."):
        print("마침표로 끝납니다.")
    else:
        print("마침표로 끝나지 않습니다.")


main()
