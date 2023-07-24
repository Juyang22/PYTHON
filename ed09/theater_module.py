# 사람 수에 따른 영화 가격을 계산하는 함수 3개 정의
# 일반, 조조, 군인 할인

# 일반
def price(people):
    print('{0}명, 영화표 가격은 {1}원입니다.'.format(people, people * 15000))


# 조조
def price_morning(people):
    print('{0}명, 영화표 가격은 {1}원입니다.'.format(people, people * 9000))


# 군인
def price_soldier(people):
    print('{0}명, 영화표 가격은 {1}원입니다.'.format(people, people * 100))
