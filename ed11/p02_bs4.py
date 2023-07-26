from bs4 import BeautifulSoup


def main():
    # HTML
    html_doc = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>BeautifulSoup4 예제</title>
    </head>
    <body>
        <div id="container">
            <h1>HTML 파싱 예제</h1>
            <ul>
                <li>사과</li>
                <li>바나나</li>
                <li>오렌지</li>
            </ul>
        </div>
    </body>
    </html>
    '''

    # 객체 생성
    soup = BeautifulSoup(html_doc, 'html.parser')

    # 태그 정보 가져오기
    title = soup.title

    # 태그 내용 출력
    print(f'title : {title}')  # title : <title>BeautifulSoup4 예제</title> -> html tag
    print(f'title : {title.text}')  # title : BeautifulSoup4 예제

    h1 = soup.h1
    print(f'h1 : {h1.text}')  # h1 : HTML 파싱 예제

    # li []
    li_lst = soup.find_all('li')
    for li in li_lst:
        print(f'li : {li.text}')


main()
