'''
https://docs.python.org/ko/3/reference
'''


def main():
    print("나는 {}살입니다.".format(22))  # 나는 22살입니다.
    print("나는 {}색과 {}색을 좋아해요.".format("빨간", "파란"))  # 나는 빨간색과 파란색을 좋아해요.

    # 인덱스는 0번부터 시작
    print("나는 {0}색과 {1}색을 좋아해요.".format("빨간", "파란"))  # 나는 빨간색과 파란색을 좋아해요.
    print("나는 {1}색과 {0}색을 좋아해요.".format("빨간", "파란"))  # 나는 파란색과 빨간색을 좋아해요.

    # print("문자열{이름1} 문자열{이름2}".format(이름 = 값, 이름2 = 값))

    print("나는 {age}살이고, {color}색을 좋아해요.".format(age=22, color="노란"))  # 나는 22살이고, 노란색을 좋아해요.
    print("나는 {age}살이고, {color}색을 좋아해요.".format(color="노란", age=22))  # index 순서 상관 X

    # f 문자열 사용: python 3.6 이상
    # print(f"문자열 {변수명1} 문자열 {변수명2}")
    age = 22
    color = "보라"
    print(f"나는 {age}살이고, {color}색을 좋아해요.")  # 나는 22살이고, 보라색을 좋아해요.


main()
