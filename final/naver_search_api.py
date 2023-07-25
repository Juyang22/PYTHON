import json
# 네이버 검색 API 예제 - 블로그 검색
import os
import sys
import urllib.request

client_id = "5sDTGfFr6bMrGr_jG99Y"
client_secret = "36k1aoIWy8"


def naver_blog_search(keyword):
    response_body = None

    encText = urllib.parse.quote(keyword)
    url = "https://openapi.naver.com/v1/search/blog?query=" + encText  # JSON 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText  # XML 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)

    return response_body


if __name__ == '__main__':
    keyword = input('검색어를 입력하세요.>')
    string_json = naver_blog_search(keyword)
    # JSON parsing
    data = json.loads(string_json)

    # print(type(data), data)  # <class 'dict'>

    # dictionary에서 items 찾기
    jsonArray = data.get('items')

    for dic_array in jsonArray:  # items 내에서 데이터 출력
        # print(type(dic_array), dic_array)  # <class 'dict'>
        title = dic_array.get('title')  # 제목
        bloggername = dic_array.get('bloggername')  # 블로거명
        postdate = dic_array.get('postdate')  # 등록일
        print('title : {0}, bloggername : {1}, postdate : {2}'.format(title, bloggername, postdate))
