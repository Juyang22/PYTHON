'''
https://docs.python.org/ko/3/reference
'''

def print_kwargs(**kwargs):
    print(kwargs, type(kwargs))  # {'a': 1} <class 'dict'>


def main():
    print_kwargs(a=1)  # {'a': 1} <class 'dict'>
    print_kwargs(name='pooh', age=23)  # {'name': 'pooh', 'age': 23} <class 'dict'>

main()
