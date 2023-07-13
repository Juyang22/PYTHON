'''
https://docs.python.org/ko/3/reference
'''
from random import *

def main():
    celsius = 10     # 섭씨 온도
    fahrenheit = 0   # 화씨 온도

    fahrenheit = (celsius * 9 / 5) + 32

    print('섭씨 온도 : {}'.format(celsius))
    print('화씨 온도 : {}'.format(fahrenheit))

    # 섭씨 온도 : 10
    # 화씨 온도 : 50.0


main()
