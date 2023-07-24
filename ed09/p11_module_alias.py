'''
https://docs.python.org/ko/3/reference
'''

import theater_module as tm # 모듈에 as 부여해서 가져오기: 모듈 이름 간략히 표현 가능


def main():
    tm.price(3)  # 일반 3명 영화 관람
    tm.price_morning(4)  # 조조 4명
    tm.price_soldier(5)  # 군인 5명


main()
