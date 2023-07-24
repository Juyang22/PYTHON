'''
https://docs.python.org/ko/3/reference
'''

# travel_temp.thailand 모듈의 ThailandPackage 클래스
from travel_temp.thailand import ThailandPackage

def main():
    # travel_temp 패키지의 thailand 모듈의 ThailandPackage 클래스
    trip_to = ThailandPackage()
    trip_to.detail()  # [태국 3박 5일 패키지] 방콕, 파타야 여행 50만원!!

main()
