'''
https://docs.python.org/ko/3/reference
'''

# 일반 함수
def add(a, b):
    return a + b

add_lam = lambda a, b : a + b

def main():
    result = add(12, 14)
    print(result)  # 26
    result = add_lam(2, 4)
    print(result)  # 6

main()
