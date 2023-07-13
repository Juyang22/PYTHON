'''
https://docs.python.org/ko/3/reference
'''

from math import *    # math 모듈의 모든 기능을 가져다 씀
# from math import ceil, floor, sqrt    # math 모듈에서 ceil, floor, sqrt를 가져다 씀

def main():
    result = floor(4.99)
    print(result)  # 4.99의 버림 -> 4

    result = ceil(3.14)
    print(result)  # 3.14의 올림 -> 4

    result = sqrt(16)
    print(result)  # 16의 제곱근 -> 4.0


main()
