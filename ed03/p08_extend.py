'''
https://docs.python.org/ko/3/reference
'''


def main():
    mix_list = ['이상무무', True, 20, [5, 2, 4, 1]]
    print(mix_list)  # ['이상무무', True, 20, [5, 2, 4, 1]]

    print("-" * 50)

    mix2_list = ['이상무', True, 20]
    num_list  = [1, 3, 2]

    # extend : 서로 다른 리스트 합치기
    num_list.extend(mix2_list)

    print(num_list)   # [1, 3, 2, '이상무', True, 20] -> num_list에 mix2_list가 합쳐짐
    print(mix2_list)  # ['이상무', True, 20]

main()
