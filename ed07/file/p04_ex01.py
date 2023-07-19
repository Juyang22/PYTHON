'''
https://docs.python.org/ko/3/reference
'''


def main():
    # class.txt 파일 생성
    with open("class.txt", "w", encoding="utf-8") as class_file:
        class_file.write("초록반 5세 20명 파랑반 6세 18명 노랑반 7세 22명")

    with open("class.txt", "r", encoding="utf-8") as class_file:
        class_str = class_file.read()
        print(class_str.split())

        print("-" * 50)

        class_list = class_str.split()
        for str_data in class_list:
            if str_data.endswith("명"):
                print(str_data)
            else:
                print(str_data, end=" ")

    # ['초록반', '5세', '20명', '파랑반', '6세', '18명', '노랑반', '7세', '22명']
    # --------------------------------------------------
    # 초록반 5세 20명
    # 파랑반 6세 18명
    # 노랑반 7세 22명

main()
