'''
숫자형 : 정수, 실수
'''
from builtins import type


def main():
    # 정수형
    num = 123
    print(num)  # 123
    # num:123, type<class 'int'>
    print("num:{0}, type{1}".format(num, type(num)))

    # 실수형
    fNum = 1.2
    print(fNum)  # 1.2
    # fNum:1.2, type:<class 'float'>
    print("fNum:{0}, type:{1}".format(fNum, type(fNum)))

    fNum = 4.12E10  # 지수 표현 방식 4.12 * 10^10
    print("fNum:{1}, {0}".format(fNum, type(fNum)))  # fNum:<class 'float'>, 41200000000.0

    fNum = 4.12E-10
    print(fNum)  # 4.12e-10


main()