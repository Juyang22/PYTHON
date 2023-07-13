'''
https://docs.python.org/ko/3/reference
'''


def main():
    sentence01 = '나는 소년입니다.'
    print(sentence01, type(sentence01))  # 나는 소년입니다. <class 'str'>

    sentence02 = "나는 소년입니다."
    print(sentence02, type(sentence02))  # 나는 소년입니다. <class 'str'>

    sentence03 = """
    나는 소년입니다.
    파이썬은 쉽습니다."""
    print(sentence03, type(sentence03))  # 나는 소년입니다.
                                         # 파이썬은 쉽습니다. <class 'str'>

main()
