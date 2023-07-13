'''
https://docs.python.org/ko/3/reference
'''
from random import *    # random 모듈에 있는 모든 기능 사용

def main():
    # 0 <= x < 1
    print(random())  # 0.2271072168797852
    print(random())
    print(random())

    print("-" * 50)

    print(random() * 10)
    print(int(random() * 45) + 1)

    print("-" * 50)
    print(randrange(1, 46))  # 1 <= x < 46 난수 생성
    print(randint(1, 45))    # 1 <= x <= 45 난수 생성

main()