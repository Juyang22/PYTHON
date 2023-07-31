"""
파일명: search.py
생성자: PCWK
생성일: 2023-07-31
"""


class SearchDiv:
    """ 검색 """
    def __init__(self, search_div='', search_word=''):
        self.search_div = search_div
        self.search_word = search_word

    # 인스턴스 변수들을 문자열로 변환 출력
    def __str__(self):
        return 'search_div : {}, search_word : {}'.format(self.search_div, self.search_word)