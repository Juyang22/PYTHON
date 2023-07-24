def save_battery(level):
    print('배터리 잔량 : {0}%'.format(level))

    if level > 30:
        print('일반 모드로 사용합니다.')
    elif level > 5:
        print('절전 모드로 사용합니다.')
    else:
        raise Exception('배터리가 부족해 스마트폰을 종료합니다.')


def main():
    try:
        save_battery(75)
        save_battery(25)
        save_battery(3)
    except Exception as err:
        print('Exception : ', err)


main()
