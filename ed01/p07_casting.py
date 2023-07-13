'''
 문자형 : str()
 정수형 : int()
 실수형 : float()
'''


def main():
    x = 3
    print("{}, {}".format(x, type(x)))  # 3, <class 'int'>

    x = "3"
    print("{}, int(x) : {}".format(x, type(int(x))))  # 3, int(x) : <class 'int'>

    x = 3.5
    # 실수를 int로 캐스팅하면 정수 부분만 출력
    print("{}, int(x) : {}".format(int(x), type(int(x))))  # 3, int(x) : <class 'int'>

    x = '삼'
    # print("{}, int(x) : {}".format(int(x), type(int(x))))
    # ValueError: invalid literal for int() with base 10: '삼'

    # float
    print(float("3.5"))  # 3.5

    # 정수 3
    print(float(3))  # 3.0

main()
