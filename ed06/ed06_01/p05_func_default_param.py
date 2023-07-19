'''
https://docs.python.org/ko/3/reference
'''

# 마트에서 상품을 구매하는 경우
def buy(item1, item2='음료수'):
    print(item1, item2)

# non-default parameter follows default parameter
# def buy2(item2='음료수', item1):
#     print(item1, item2)

def main():
    buy('아아')


main()
