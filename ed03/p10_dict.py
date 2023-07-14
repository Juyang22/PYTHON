'''
https://docs.python.org/ko/3/reference
'''


def main():
    # dictionary
    cabinet = {3: '푸', 100: '피글렛'}

    # data 꺼낼 때 : dict[key]로 접근
    print(cabinet[3])    # key: 3에 해당하는 값 -> '푸'
    print(cabinet[100])  # 피글렛

    print("-" * 50)

    # dict.get(key)
    print(cabinet.get(3))  # 푸

    # dict에 없는 key 사용해보기
    print(cabinet.get(99, '없어용'))  # 없어용

    # key in dict : key값 유무 확인
    print(3 in cabinet)   # True
    print(99 in cabinet)  # False


main()
