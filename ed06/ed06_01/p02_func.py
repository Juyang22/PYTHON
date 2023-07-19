'''
https://docs.python.org/ko/3/reference
'''

# 은행 계좌 개설하기
def open_account():
    print("새로운 계좌를 개설합니다.")

def deposit(balance, money):  # 입금 처리
    print("{0}원을 입금했습니다. 잔액은 {1}원입니다.".format(money, balance + money))
    return balance + money  # 입금 후 잔액 정보 반환

def withdraw(balance, money):  # 출금 처리
    if balance >= money:  # 잔액이 출금 금액보다 많으면
        print("{0}원을 출금했습니다. 잔액은 {1}원입니다.".format(money, balance - money))
        return balance - money  # 출금 후 잔액 정보 반환
    else:  # 잔액이 출금 금액보다 많지 않으면
        print("잔액이 부족합니다. 잔액은 {0}원입니다.".format(balance))
        return balance


def main():
    open_account()  # 계좌 개설

    print("-" * 50)

    # 입금
    balance = 0  # 초기 잔액, parameter의 balance와는 연관 X
    print("입금 전 잔액: {0}원".format(balance))
    balance = deposit(balance, 1000)  # 1000원 입금
    print("입금 후 잔액: {0}원".format(balance))

    print("-" * 50)

    # 출금: 출금액이 잔액보다 큰 경우(2000원), 출금액이 잔액보다 작은 경우(500원)
    balance = withdraw(balance, 2000)
    balance = withdraw(balance, 500)
    print("출금 후 잔액: {0}원".format(balance))


main()
