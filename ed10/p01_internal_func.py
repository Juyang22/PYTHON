'''
https://docs.python.org/ko/3/reference
'''

import random


def main():
    # 내장 함수: import 없이 사용 가능
    # language = input('어떤 언어를 좋아하세요? > ')
    # print('{0}은 아주 좋은 언어입니다.'.format(language))

    # ------------------------------------------------------------
    # dir() : 어떤 객체를 param으로 전달하면, 그 객체가 사용할 수 있는
    #         변수, 함수 정보를 return

    print(dir(random))

    lst = [12, 14, 17]
    print(dir(lst))

    name = 'PCWK'
    print(dir(name))


main()
