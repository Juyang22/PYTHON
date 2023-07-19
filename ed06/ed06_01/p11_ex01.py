'''
https://docs.python.org/ko/3/reference
'''


def std_weight(height, gender):
    height_in_meter = height * 0.01
    std_weight = 0

    if gender == '남자':
        std_weight = round(height_in_meter ** 2 * 22, 2)
    elif gender == '여자':
        std_weight = round(height_in_meter ** 2 * 21, 2)
    print('키 {0}cm {1}의 표준 체중은 {2}kg입니다.'.format(height, gender, std_weight))
    return std_weight


def main():
    std_weight(175, '남자')
    std_weight(185, '남자')
    std_weight(174, '여자')

main()
