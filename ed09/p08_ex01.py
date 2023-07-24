class SoldOutError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


def main():
    chicken = 10  # 남은 치킨 수
    waiting = 1   # 대기 번호, 1부터 시작

    while True:
        try:
            print("[남은 치킨 : {0}]".format(chicken))
            order = int(input("치킨을 몇 마리 주문하시겠습니까? > "))

            if order < 1:
                raise ValueError('값을 잘못 입력하셨습니다.')

            if order > 10:
                print('최대 주문 수량은 10마리입니다.')

            if order > chicken:  # 남은 치킨보다 주문량이 많을 때
                print("재료가 부족합니다.")
            else:
                print("[대기번호 {0}] {1}마리를 주문했습니다.".format(waiting, order))
                waiting += 1  # 대기 번호 1 증가
                chicken -= order  # 주문 수만큼 남은 치킨 감소

            if chicken == 0:
                raise SoldOutError('재료가 소진되어 더 이상 주문을 받지 않습니다.')

        except ValueError as err:
            print('ValueError : ', err)

        except SoldOutError as err:
            print('SoldOutError : ', err)
            print('프로그램을 종료합니다.')
            break


main()
