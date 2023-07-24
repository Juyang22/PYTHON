'''
https://docs.python.org/ko/3/reference
'''


def main():
    print('나누기 전용 계산기입니다.')
    try:
        nums = []

        nums.append(int(input('첫 번째 숫자를 입력하세요.>')))
        nums.append(int(input('두 번째 숫자를 입력하세요.>')))

        # nums.append(nums[0]/nums[1])

        print('{0}/{1} = {2}'.format(nums[0], nums[1], nums[2]))
        # IndexError: list index out of range

    except ValueError:
        print('오류 발생! 잘못된 값을 입력했습니다.')
    except ZeroDivisionError as err:
        print('ZeroDivisionError : ', err)
    except Exception as err:
        print(err)

    print('프로그램 종료!')


main()
