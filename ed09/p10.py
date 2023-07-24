'''
https://docs.python.org/ko/3/reference
'''

import theater_module  # 모듈 가져오기


def main():
    theater_module.price(3)  # 일반 3명 영화 관람
    theater_module.price_morning(4)  # 조조 4명
    theater_module.price_soldier(5)  # 군인 5명


main()
