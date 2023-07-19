'''
https://docs.python.org/ko/3/reference
'''

# 전역 변수
glasses_value = 10  # 전체 3D 안경 개수: 10개

def rent_return(glasses, people):  # 3D 안경을 대여한 관객 수
    glasses = glasses - people  # 잔여 안경 개수 = 전체 개수 - 대여한 개수
    print('[함수 내부] 남은 3D 안경 개수: {}'.format(glasses))
    return glasses

def main():
    print("전체 3D 안경 개수: {}".format(glasses_value))  # 전역 변수 호출
    glasses = rent_return(glasses_value, 2)  # 3D 안경을 관객 2명에게 대여
    print("남은 3D 안경 개수: {}".format(glasses))

    # 전체 3D 안경 개수: 10
    # [함수 내부] 남은 3D 안경 개수: 8
    # 남은 3D 안경 개수: 8

main()
