'''
https://docs.python.org/ko/3/reference
'''

from theater_module import price, price_morning, price_soldier  # theater_module에서 필요한 기능 나열


def main():
    price(3)  # 일반 3명 영화 관람
    price_morning(4)  # 조조 4명
    price_soldier(5)  # 군인 5명


main()
