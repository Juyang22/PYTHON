'''
https://docs.python.org/ko/3/reference
'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# clipboard 사용 외부 모듈
import pyperclip3


def naver_login():
    url = 'https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/'

    # 웹 드라이버 실행
    browser = webdriver.Chrome()

    # 접속
    browser.get(url)
    user_id = 'calmate77'
    user_pw = 'calmate77!'

    # id
    id_textinput = browser.find_element(By.ID, 'id')
    id_textinput.click()

    pyperclip3.copy(user_id)  # 클립보드로 user_id값 가져옴
    id_textinput.send_keys(Keys.CONTROL, 'v')
    time.sleep(1)

    # pw
    pw_textinput = browser.find_element(By.ID, 'pw')
    pw_textinput.click()

    pyperclip3.copy(user_pw)
    pw_textinput.send_keys(Keys.CONTROL, 'v')
    time.sleep(1)

    # 로그인 버튼: log.login
    btn_login = browser.find_element(By.ID, 'log.login')
    btn_login.click()  # 버튼 클릭
    time.sleep(5)  # 5초

    # 드라이버 종료
    browser.quit()


def main():
    naver_login()


main()
