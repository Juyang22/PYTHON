'''
https://docs.python.org/ko/3/reference
'''
from bs4 import BeautifulSoup


def main():
    html_doc = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>BeautifulSoup4 CSS ID 파싱 예제</title>
    </head>
    <body>
        <div id="container">
            <h1>HTML 파싱 예제</h1>
            <ul>
                <li id="fruit1">사과</li>
                <li id="fruit2">바나나</li>
                <li id="fruit3">오렌지</li>
            </ul>
            <ul>
                <li class="fruit">사과</li>
                <li class="fruit">바나나</li>
                <li class="fruit">오렌지</li>
            </ul>
            
        </div>
    </body>
    </html>
    '''

    # BeautifulSoup 객체 생성
    soup = BeautifulSoup(html_doc, 'html.parser')

    # CSS id 선택자로 요소 가져오기: find, select_one
    fruit1 = soup.find(id="fruit1")
    fruit2 = soup.select_one("#fruit2")

    # 요소 출력
    print(f'fruit1 : {fruit1.text}')  # fruit1 : 사과
    print(f'fruit2 : {fruit2.text}')  # fruit2 : 바나나

    # CSS class 선택자로 요소 가져오기
    fruits = soup.select(".fruit")  # class 이름이 fruit인 모든 요소 선택

    for fruit in fruits:
        print(fruit.text)  # 사과\n 바나나\n 오렌지\n

main()
