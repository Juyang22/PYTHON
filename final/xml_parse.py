'''
https://docs.python.org/ko/3/reference
'''

# XML 문서의 각 요소(Element)
import xml.etree.ElementTree as ET

def main():
    xml_data = '''
    <bookstore>
        <book>
            <title>점프 투 파이썬</title>
            <author>박응용</author>
            <year>2022</year>
        </book>
        <book>
            <title>파이썬 입문</title>
            <author>나도코딩</author>
            <year>2022</year>
        </book>
    </bookstore>
    '''

    # XML 데이터 파싱
    # ET.parse(파일) -> 파일에서 읽을 때
    root = ET.fromstring(xml_data)

    # Element 클래스를 사용하여 요소의 정보 출력
    print('태그 이름:', root.tag)  # 태그 이름:  bookstore
    print('텍스트 내용:', root.text)  # 텍스트 내용:
    print('속성:', root.attrib)  # 속성:  {}

    # 하위 요소 정보
    for child in root:
        print('하위 요소 태그 이름:', child.tag)  # 하위 요소 태그 이름: book
        print('하위 요소 텍스트 내용:', child.text)  # 하위 요소 텍스트 내용:
        print('하위 요소 속성:', child.attrib)  # 하위 요소 속성:  {}

    # 첫 번째 book element의 하위 element 찾기
    title = root.find("book/title").text
    author = root.find("book/author").text
    year = root.find("book/year").text

    print('첫 번째 책 정보')
    print(f'제목: {title}')
    print(f'저자: {author}')
    print(f'출판연도: {year}')

    print('-' * 50)

    # 모든 book element의 하위 요소 찾기
    books = root.findall("book")

    for book in books:
        title = book.find('title').text
        author = book.find('author').text
        year = book.find('year').text

        print(f'제목:{title}')
        print(f'저자:{author}')
        print(f'출판연도:{year}')
        print('=========================')
main()
