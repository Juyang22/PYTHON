'''
https://docs.python.org/ko/3/reference
'''


def main():
    # sort() : 정렬(default = 오름차순)
    num_list = [5, 2, 4, 3, 1]
    print(num_list)  # [5, 2, 4, 3, 1]

    # 오름차순 정렬
    num_list.sort()
    print(num_list)  # [1, 2, 3, 4, 5]

    # 내림차순 정렬
    num_list.sort(reverse=True)
    print(num_list)  # [5, 4, 3, 2, 1]

    # reverse() : 값의 순서 뒤집기
    num_list.reverse()
    print(num_list)  # [1, 2, 3, 4, 5]

    print("-" * 50)
    # sorted() : 원본이 바뀌지 않고 새로운 list 반환
    my_list = [1, 3, 2]
    my_list.sort()
    print(my_list)  # [1, 2, 3] -> 원본이 변경됨

    print("-" * 50)
    your_list = [1, 3, 2]

    new_list = sorted(your_list)
    print(your_list)  # [1, 3, 2]
    print(new_list)   # [1, 2, 3]


main()
