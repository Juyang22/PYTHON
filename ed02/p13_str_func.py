'''
https://docs.python.org/ko/3/reference
'''


def main():
    python = 'Python is Amazing'

    print(python.lower())  # 전체를 소문자로: python is amazing
    print(python.upper())  # 전체를 대문자로: PYTHON IS AMAZING

    # 특정 index의 문자열이 대문자/소문자인지 확인
    print(python[1:3].islower())  # index [1]부터 [2]까지 소문자인지 확인 -> True

    # 'Python' -> 'Java'로 변경
    print(python.replace("Python", "Java"))  # Java is Amazing


main()
