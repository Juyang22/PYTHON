'''
https://docs.python.org/ko/3/reference
'''

import json

def read_json():
    # JSON 문자열
    json_string = '{"name":"Lee", "age":22, "city":"Seoul"}'

    # JSON 문자열 파싱
    parsed_json = json.loads(json_string)  # parsed_json:{'name': 'Lee', 'age': 22, 'city': 'Seoul'}

    print('parsed_json:{0}'.format(parsed_json))
    print('parsed_json type:{0}'.format(type(parsed_json)))  # parsed_json type:<class 'dict'>
    # parsing 이후의 데이터는 dictionary

    print('name:{0}'.format(parsed_json['name']))  # name:Lee

def main():
    # read_json()

    data = None

    # JSON 파일 읽기
    with open('naver_blog_20230725.json') as json_file:
        data = json.load(json_file)

    # print(type(data), data)  # <class 'dict'>

    # JSON parsing
    jsonArray = data.get('items')

    for dic_array in jsonArray:
        # print(type(dic_array), dic_array)  # <class 'dict'>
        title = dic_array.get('title')
        bloggername = dic_array.get('bloggername')
        postdate = dic_array.get('postdate')
        print('title : {0}, bloggername : {1}, postdate : {2}'.format(title, bloggername, postdate))





main()
