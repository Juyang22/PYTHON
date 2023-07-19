'''
https://docs.python.org/ko/3/reference
'''

def profile(name, age=20, main_lang='Java'):
    print("이름: {0}\t 나이: {1}\t 주 사용 언어: {2}".format(name, age, main_lang))

def main():
    #profile("이상뮤", 22, "Java")
    #profile("룰루", 24, "Python")
    profile("이상뮤")
    profile("라이츄")
    profile("스누피", 22)
    profile("루시", 22, "Python")


main()
