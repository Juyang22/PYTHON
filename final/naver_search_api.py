import json
import xml.etree.ElementTree as ET
# 네이버 검색 API 예제 - 블로그 검색
import os
import sys
import urllib.request

client_id = "5sDTGfFr6bMrGr_jG99Y"
client_secret = "36k1aoIWy8"


def naver_blog_search(keyword, data_type='JSON'):
    response_body = None

    encText = urllib.parse.quote(keyword)
    if data_type.upper() == 'JSON':
        url = "https://openapi.naver.com/v1/search/blog?query=" + encText  # JSON 결과
    else:
        url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText  # XML 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if rescode == 200:
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)

    return response_body


# if __name__ == '__main__':
    # keyword = input('검색어를 입력하세요.>')
    # data_type = 'XML'
    #
    # if data_type == 'JSON':
    #     string_json = naver_blog_search(keyword, data_type)
    #     # JSON parsing
    #     data = json.loads(string_json)
    #
    #     # print(type(data), data)  # <class 'dict'>
    #
    #     # dictionary에서 items 찾기
    #     jsonArray = data.get('items')
    #     for dic_array in jsonArray:  # items 내에서 데이터 출력
    #         # print(type(dic_array), dic_array)  # <class 'dict'>
    #         title = dic_array.get('title')  # 제목
    #         bloggername = dic_array.get('bloggername')  # 블로거명
    #         postdate = dic_array.get('postdate')  # 등록일
    #         print('title : {0}, bloggername : {1}, postdate : {2}'.format(title, bloggername, postdate))
    # else:
    #     try:
    #         string_xml = naver_blog_search(keyword, data_type)
    #         # print('string_xml\n', string_xml)
    #
    #         root = ET.fromstring(string_xml)
    #         print('root type: {}', format(root))  # root type: {} <Element 'rss' at 0x038D6D98>
    #
    #         channels = root.findall('channel/item')
    #         # for item in root.findall('.//item')
    #         for item in channels:
    #             title = item.find('title').text
    #             link = item.find('link').text
    #             description = item.find('description').text
    #             blogger_name = item.find('bloggername').text
    #             blogger_link = item.find('bloggerlink').text
    #             post_date = item.find('postdate').text
    #
    #             print(f'제목: {title}')
    #             print(f'게시글 링크: {link}')
    #             print(f'설명: {description}')
    #             print(f'블로그 이름: {blogger_name}')
    #             print(f'블로그 링크: {blogger_link}')
    #             print(f'작성일: {post_date}')
    #
    #             print('=' * 50)
    #
    #     except Exception as e:
    #         print('Exception : ' + str(e))
