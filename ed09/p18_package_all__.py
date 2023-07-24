'''
https://docs.python.org/ko/3/reference
'''

from travel_temp import *

def main():
    # Unresolved reference 'vietnam' 오류 발생 -> __init__.py 설정
    # trip_to = vietnam.VietnamPackage()
    trip_to = thailand.ThailandPackage()
    trip_to.detail()  # [태국 3박 5일 패키지] 방콕, 파타야 여행 50만원!!


main()
