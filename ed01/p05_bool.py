'''
 불 자료형 : 참(True) / 거짓(False)
'''


def main():
    x = True  # 첫 글자 대문자로!!
    y = False

    # format에 순서 index 생략 시 순서대로 출력
    print("{} {}".format(x, type(x)))  # True <class 'bool'>
    print("{} {}".format(y, type(y)))  # False <class 'bool'>

    print(5 > 10)  # False
    print(5 < 10)  # True

    # not 연산자: True -> False, False -> True
    print(not True)   # False
    print(not False)  # True

main()
