'''
https://docs.python.org/ko/3/reference
'''


def main():
    subway = ['이상뮤', '홍기동', '토끼']
    print(subway)

    subway.append('이상뮤')  # 이상뮤 추가
    print(subway) # ['이상뮤', '홍기동', '토끼', '이상뮤']

    print(subway.count('이상뮤'))  # 2


main()
