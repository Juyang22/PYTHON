class BigNumberError(Exception):  # 사용자 정의 예외, Exception 상속
    def __init__(self, msg):  # 스페셜 메서드, 던더 메서드(dunder method)
        self.msg = msg

    def __str__(self):
        return '[오류 코드 : 001] ' + self.msg  # 메시지 가공


# 계산기 프로그램
def main():
    print('나누기 전용 계산기입니다.')
    try:
        num1 = int(input('첫 번째 숫자를 입력하세요.>'))
        num2 = int(input('두 번째 숫자를 입력하세요.>'))

        if num1 >= 10 or num2 >= 10:  # 입력 받은 숫자가 두 자리이면
            raise BigNumberError("입력값: {0}, {1}".format(num1, num2))  # 예외 발생

        print('{0}/{1} = {2}'.format(num1, num2, int(num1/num2)))
        # ValueError: invalid literal for int() with base 10: '삼'
    except ValueError as err:
        print('오류 발생! 잘못된 값을 입력했습니다.', err)
    except ZeroDivisionError as err:
        print('ZeroDivisionError : ', err)
    except BigNumberError as err:
        print('BigNumberError : ', err)  # BigNumberError : 입력값: 10, 5
    finally:    # 자원 반납, 파일 open, close, DB 연결, 종료 등
        print('계산기를 사용해 주셔서 감사합니다.')

    print('프로그램 종료!')


main()
