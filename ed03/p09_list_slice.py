'''
https://docs.python.org/ko/3/reference
'''


def main():
    num_list = [1, 2, 3, 4, 5]
    print(num_list)  # [1, 2, 3, 4, 5]

    print(num_list[0:2])  # [0] <= x < [2] -> [1, 2]

    # 시작부터 [2]까지 출력
    num_01 = num_list[:2]
    print(num_01)   # [1, 2]

    # [2]부터 끝까지
    num_02 = num_list[2:]
    print(num_02)  # [3, 4, 5]

    print("-" * 50)

    # 중첩 list slicing
    nest_list = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
    print(nest_list)  # [1, 2, 3, ['a', 'b', 'c'], 4, 5]
    print(nest_list[2:5])  # 3, ['a', 'b', 'c'], 4

    print(nest_list[3][:2])  # ['a', 'b'] -> nest_list[3]도 하나의 배열로 생각하면 ok

    # list 연산
    num01_list = [1, 2, 3]
    num02_list = [4, 5, 6]

    # '+' : list 결합
    print(num01_list + num02_list)  # [1, 2, 3, 4, 5, 6]

    # '*' : 곱한 수만큼 list 반복
    print(num01_list * 3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

    # list 길이 구하기
    print(len(num01_list))  # 3


main()
