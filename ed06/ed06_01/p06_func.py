'''
https://docs.python.org/ko/3/reference
'''

def add(a, b):
    return a + b
def main():
    result = add(a=12, b=14)
    print(result)  # 26, 매개변수 지정해서 호출하기
    result = add(b=14, a=12)
    print(result)  # 26

main()
