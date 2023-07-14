'''
https://docs.python.org/ko/3/reference
'''


def main():
    subway = ['Java', 'Oracle', 'HTML', 'CSS', 'Javascript', 'JSP', 'Spring']
    #['Java', 'Oracle', 'HTML', 'CSS', 'Javascript', 'JSP', 'Spring']
    print(subway)

    # append : list 마지막에 추가
    subway.append('Django')
    print(subway)  # ['Java', 'Oracle', 'HTML', 'CSS', 'Javascript', 'JSP', 'Spring', 'Django']

    # insert : 특정 index에 추가
    subway.insert(4, 'jQuery')
    print(subway)  # ['Java', 'Oracle', 'HTML', 'CSS', 'jQuery', 'Javascript', 'JSP', 'Spring', 'Django']

    # pop : 값 꺼낸 후 기존 리스트에서 제거
    print(subway.pop())  # Django
    print(subway)  # ['Java', 'Oracle', 'HTML', 'CSS', 'jQuery', 'Javascript', 'JSP', 'Spring']

    print(subway.pop())  # Spring
    print(subway)  # ['Java', 'Oracle', 'HTML', 'CSS', 'jQuery', 'Javascript', 'JSP']

    # clear : list의 모든 데이터 삭제
    subway.clear()
    print(subway)  # []


main()
