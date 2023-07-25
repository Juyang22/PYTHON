def say_hello(to):
    print('안녕, {}?'.format(to))


def say_goodbye(to):
    print('또 만나, {}!'.format(to))


if __name__ == "__main__":  # 모듈에서 직접 실행
    say_hello('파이썬')
    say_goodbye('주양')
