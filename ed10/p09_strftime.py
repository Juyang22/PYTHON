'''
https://docs.python.org/ko/3/reference
'''
import time
import datetime

# %Y	연도(year)
# %m	월(month)
# %d	일(day)
# %H	시간(hour)
# %M	분(minute)
# %S	초(second)


def main():
    # yyyy-mm-dd H:M:S
    print(time.strftime('%Y-%m-%d %H:%M:%S'))  # 연-월-일 시:분:초
    # 2023-07-25 10:38:05

    # 오늘 날짜 출력
    print('오늘 날짜 출력', datetime.date.today()) # 오늘 날짜 출력 2023-07-25

    # 두 날짜 사이의 차이를 계산하는 함수: timedelta()
    # 오늘로부터 100일째 되는 날 계산
    today = datetime.date.today()  # 오늘 날짜
    td = datetime.timedelta(days=100)   # 100일째 되는 날짜
    print('우리가 만난 지 100일은', today + td)  # 우리가 만난 지 100일은 2023-11-02


main()
