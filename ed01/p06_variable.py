'''
 변수
'''


def main():
    # 문자열 연산 : '+'
    name = "연탄이"
    animal = '개'
    age = 4  # 숫자와 문자열 결합은 숫자를 문자열로 캐스팅해야 함!
    is_male = True  # bool과 문자열 결합도 문자열로 캐스팅 필요!

    print("반려동물을 소개해주세요.")
    print("우리 집 반려동물은 " + animal + "인데, 이름이 " + name + "예요.")
    # TypeError: can only concatenate str (not "int") to str
    # print(name + "는 " + age + "살이고, 산책을 아주 좋아해요.")
    print(name + "는 " + str(age) + "살이고, 산책을 아주 좋아해요.")
    print(name + "는 " + str(is_male) + " 수컷인가요?")
    print("네.")

main()
