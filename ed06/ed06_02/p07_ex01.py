'''
https://docs.python.org/ko/3/reference
'''

week = 0

def main():
    for i in range(1, 51):
        file_name = f"{i}주차.txt"
        # file_name = "%d주차.txt" %(i)
        print(file_name)

        report_file = open(file_name, "w", encoding="utf8")

        print("- {0}주차 주간보고 -".format(i), file=report_file)
        print("부서 : ", file=report_file)
        print("이름 : ", file=report_file)
        print("업무 요약 : ", file=report_file)

        report_file.close()  # 파일 객체 닫기(자원 반납)

main()
