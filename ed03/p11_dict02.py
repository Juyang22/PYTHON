'''
https://docs.python.org/ko/3/reference
'''


def main():
    cabinet = {'A-3': '야호', 'B-100': '냐호'}
    print(cabinet)  # {'A-3': '야호', 'B-100': '냐호'}

    # dict[new key] = value : 값 추가
    cabinet['C-3'] = '장마'
    print(cabinet)  # {'A-3': '야호', 'B-100': '냐호', 'C-3': '장마'}

    # dict[old key] = value : 값 변경
    cabinet['B-100'] = '무야호'
    print(cabinet)  # {'A-3': '야호', 'B-100': '무야호', 'C-3': '장마'}

    print("-" * 50)

    # keys() : key, value값 모두 추출
    print(cabinet.keys())    # dict_keys(['A-3', 'B-100', 'C-3'])
    print(cabinet.values())  # dict_values(['야호', '무야호', '장마'])

    # items() : key, value 한꺼번에 가져오기
    print(cabinet.items())  # dict_items([('A-3', '야호'), ('B-100', '무야호'), ('C-3', '장마')])

    # clear() : 값 전체 삭제
    cabinet.clear()
    print(cabinet)  # {}

main()
