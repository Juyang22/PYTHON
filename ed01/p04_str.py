'''

'''


def main():
    print('풍선')  # 풍선
    print("나비")  # 나비
    print("나비" * 5)  # 나비나비나비나비나비
    print("10")  # 10
    # print('작은 따옴표") -> error
    # print("큰 따옴표') -> error

    # I don't want to go to school.
    print("I don't want to go to school.")  # 문자열에 작은 따옴표 출력
    #print('I don't want to go to school.') # 문법 오류

    # escape code : /'
    print('I don\'t want to go to school.')  # I don't want to go to school.

    # 여러 줄인 문자열을 변수에 대입하고 싶을 때
    # escape code : \n

    # ctrl + / : comment
    # Life is too short
    # You need python
    multiline = "Life is too short \nYou need python"
    print(multiline)

    print("-" * 50)

    # ''' '''
    multiline = '''
    Life is too short
    You need python
    '''
    print(multiline)  # 첫 줄에 Enter, 모든 줄에 indent가 들어감


main()
