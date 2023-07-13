'''
숫자형 : 진수
    # 8진수(Octal) : 숫자 0 + 영문 소문자 o (0o)
    # 16진수(Hex)  : 숫자 0 + 영문 소문자 x (0x)
'''

def main():
    num = 0o177
    print("{0}의 자료형은 {1}".format(num, type(num)))  # 127의 자료형은 <class 'int'>

    num = 0xB
    print("{0}의 자료형은 {1}".format(num, type(num)))  # 11의 자료형은 <class 'int'>

main()


