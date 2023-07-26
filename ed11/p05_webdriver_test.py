'''
https://docs.python.org/ko/3/reference
'''
from selenium import webdriver


def main():
    # web driver 객체 생성
    driver = webdriver.Chrome()
    # driver = webdriver.Chrome('C:/JSPA_0309/04_PYTHON/04_01_PYTHON/app/chromedriver-win32/chromedriver.exe')
    # -> path 형식 확인 필요

    url = 'https://www.naver.com/'

    driver.get(url)  # chrome이 열렸다 닫히면 OK


main()
