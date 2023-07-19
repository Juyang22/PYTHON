'''
https://docs.python.org/ko/3/reference
'''

def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름: {0}\t나이: {1}".format(name, age), end=" ")  # end="\n" (default)
    print(lang1, lang2, lang3, lang4, lang5, sep="\t")  #sep=" " (default)

def profile2(name, age, *language):
    print("이름: {0}\t나이: {1}".format(name, age), end=" ")
    print(language, type(language))

def main():
    # 찰리: 파이썬, 자바, C, C++, C#
    # 루시: 코틀린, 스위프트
    profile('찰리', 20, '파이썬', '자바', 'C', 'C++', 'C#')  # 이름: 찰리	나이: 20 파이썬	자바	C	C++	C#
    profile('루시', 23, '코틀린', '스위프트', '', '', '')  # 이름: 루시	나이: 23 코틀린	스위프트

    print("-" * 50)

    profile2('찰리', 20, '파이썬', '자바', 'C', 'C++', 'C#', 'Javascript')  # 이름: 찰리	나이: 20 ('파이썬', '자바', 'C', 'C++', 'C#', 'Javascript') <class 'tuple'>
    profile2('루시', 23, '코틀린', '스위프트')  # 이름: 루시	나이: 23 ('코틀린', '스위프트') <class 'tuple'>

main()
