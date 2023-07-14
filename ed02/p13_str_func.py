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

    # find(찾는 문자, 시작 인덱스, 종료 인덱스) : 찾는 문자가 없으면 -1
    # index(찾는 문자, 시작 인덱스, 종료 인덱스) : 찾는 문자 없으면 예외 발생

    print(python)

    #Python is Amazing
    find = python.find('n')
    print(find)  # 첫 번째 'n'의 위치 인덱스인 5 리턴

    find = python.find('n', find + 1)
    print(find)  # 문자 인덱스 6번째부터 찾아 n이 발견된 위치 = 15

    # 존재하지 않는 문자 찾기
    find = python.find('java')
    print(find)  # -1

    print("-" * 50)
    index = python.index("n")
    print(index)  # 5

    index = python.index("n", index + 1)
    print(index)  # 15

    index = python.index("n", 2, 6)
    print(index)  # 5

    # 찾는 문자가 없으면 오류 발생, 프로그램 종료
    # index = python.index("Spring")
    # print(index)  # ValueError: substring not found

    print("-" * 50)
    # count() : 문자열의 총 개수
    print(python)

    print(python.count("n"))  # 2
    print(python.count("v"))  # 0

    # 문자열의 길이: len (변수 또는 문자열)
    print(len(python))  # 17

main()
