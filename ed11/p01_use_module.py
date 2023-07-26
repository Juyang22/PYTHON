'''
https://docs.python.org/ko/3/reference
'''
import final.naver_search_api as naver_blog

def main():
    json_string = naver_blog.naver_blog_search('아우네돼지불백', 'JSON')
    print(json_string)


main()
