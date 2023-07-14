'''
https://docs.python.org/ko/3/reference
'''
import random
from random import shuffle, sample

def main():
    # for문 사용
    # id = []
    # for i in range(1, 21):
    #    id.append(i)  # 각 숫자를 리스트에 추가

    id = range(1, 21)
    id = list(id)
    # print(id)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    shuffle(id)
    # print(id)  # [8, 11, 5, 1, 12, 7, 17, 14, 19, 20, 2, 18, 3, 6, 4, 16, 9, 15, 13, 10]

    # 중복 없이 4명 추출
    select_data = sample(id, 4)
    # print(select_data)  # [13, 16, 17, 4]

    print("-- 당첨자 발표 --")
    print("치킨 당첨자 : {}".format(select_data[0]))   # [0] 1명
    print("커피 당첨자 : {}".format(select_data[1:]))  # [1]-[3] 3명
    print("-- 축하합니다! --")

main()
