'''
https://docs.python.org/ko/3/reference
'''
import travel_temp.thailand  # travel_temp 패키지의 thailand 모듈 사용하기

def main():
    # travel_temp 패키지의 thailand 모듈의 ThailandPackage 클래스
    trip_to = travel_temp.thailand.ThailandPackage()
    trip_to.detail()  # [태국 3박 5일 패키지] 방콕, 파타야 여행 50만원!!

main()
