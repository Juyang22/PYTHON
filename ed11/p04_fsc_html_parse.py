'''
https://docs.python.org/ko/3/reference
'''
from bs4 import BeautifulSoup
import requests
'''
금융위원회
금융 용어 사전 파싱
'''


def parse_fsc_dic(page=1):
    url = 'https://www.fsc.go.kr/in090301?curPage=' + str(page)
    lst_title = []  # 용어명
    lst_content = []  # 용어 설명
    fdic = {}  # 용어:용어 설명

    try:
        # 금융 위원회 금융 용어 접근
        print(f'url : {url}')

        response = requests.get(url)
        # https://developer.mozilla.org/ko/docs/Web/HTTP/Status
        print(f'response : {response.status_code}')
        # print(f'response.content : {response.content}')

        if response.status_code == 200:  # 성공적인 요청
            # 객체 생성
            soup = BeautifulSoup(response.content, 'html.parser')

            # 용어명
            titles = soup.select('.subject a')  # subject class 내의 a 태그
            for title in titles:
                print('용어명: ', title.text)
                lst_title.append(title.text.strip())

            # 내용
            contents = soup.select('div > .info2 p span')  # div 요소 중 클래스가 .info2인 p span 태그
            for content in contents:
                print('용어 설명: ', content.text)
                lst_content.append(content.text.strip())

            # 리스트 -> 딕셔너리 {용어명:용어 설명}
            for i in range(len(lst_title)):
                fdic[lst_title[i]] = lst_content[i]  # 딕셔너리에 추가 -> 용어명: 용어 설명

            print('fdic:{}'.format(fdic))

        else:
            print('금융위원회 용어 사전 접근 실패!')

    except Exception as e:
        print('오류 발생: ', str(e))

    return fdic


def main():
    for page in range(1, 23, 1):
        # parse_fsc_dic()  # response: <Response [200]>
        parse_fsc_dic(page)


main()
