'''
https://docs.python.org/ko/3/reference
'''

from travel_temp import vietnam  # travel_temp 패키지에서 vietnam 모듈 가져오기

def main():
    trip_to = vietnam.VietnamPackage()
    trip_to.detail()  # [베트남 3박 5일 패키지] 다낭 효도 여행 60만원!!

main()
