'''
https://docs.python.org/ko/3/reference
'''

# 전역 변수
glasses = 10  # 전체 3D 안경 개수: 10개

def rent(people):  # 3D 안경을 대여한 관객 수
    # glasses : 지역 변수(전역 변수 아님)
    # Unresolved reference 'glasses'
    global glasses  # 전역 변수 사용
    glasses = glasses - people  # 잔여 안경 개수 = 전체 개수 - 대여한 개수
    print('[함수 내부] 남은 3D 안경 개수: {}'.format(glasses))

def main():
    print("전체 3D 안경 개수: {}".format(glasses))  # 전역 변수 호출
    rent(2)  # 3D 안경을 관객 2명에게 대여
    print("남은 3D 안경 개수: {}".format(glasses))

    # 전체 3D 안경 개수: 10
    # [함수 내부] 남은 3D 안경 개수: 8
    # 남은 3D 안경 개수: 8

main()
