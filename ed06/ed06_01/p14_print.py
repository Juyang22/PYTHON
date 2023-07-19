'''
https://docs.python.org/ko/3/reference
'''


def main():
    print("스프링" + "파이썬")
    print("스프링", "파이썬")  # 스프링 파이썬: sep=" " (default)

    print("-" * 50)
    print("스프링", "파이썬", sep=", ")  # 스프링, 파이썬

    print("-" * 50)
    print("파이썬", "스프링", "자바스크립트")  # 파이썬 스프링 자바스크립트
    print("파이썬", "스프링", "자바스크립트", sep=" vs ")  # 파이썬 vs 스프링 vs 자바스크립트

main()
