'''
파일명 : smtp_naver.py
설 명  : naver smtp를 이용해서 메일 전송, csv 파일 읽어서 전송
생성일 : 2023-07-25
생성자 : PCWK
since 2023-01-01 Copyright (C) by PCWK All rights reserved.
'''
import smtplib
from email.mime.text import MIMEText


def read_addressbook():
    mail_list = []  # csv 파일 읽어서 한 줄씩 담기
    try:
        with open("address.csv", "r") as f:
            i = 0
            while True:
                line = f.readline()
                print(f' read line {line}')
                if not line:  # line이 True가 아니면
                    break

                mail_list.append(line.strip("\n"))  # \n 제거

    except IOError as e:
        pass
    finally:
        print('csv 파일 읽기 완료!')

    return mail_list


def naver_smtp(name, receive_email, p_title, p_contents):
    s = None  # smtplib.SMTP_SLL 객체
    try:
        smtp_name = 'smtp.naver.com'  # SMTP 서버명
        smtp_port = 465  # SMTP 포트
        send_email = '@naver.com'  # 보내는 메일 주소(본인)
        title = p_title  # 메일 제목
        password = ''  # 비밀번호(본인)
        recv_email = receive_email  # 받는 사람

        contents = p_contents  # 내용

        # 이름 붙여서 메일 전송
        contents = '{0}님\n{1}'.format(name, contents)

        msg = MIMEText(contents)
        msg['From'] = send_email  # 보내는 사람
        msg['To'] = recv_email    # 받는 사람
        msg['Subject'] = title    # 메일 제목

        s = smtplib.SMTP_SSL(smtp_name, smtp_port)  # SMPT 서버명, SMTP 포트
        s.set_debuglevel(True)  # debug 메시지 자세히 출력

        s.login(send_email, password)  # 본인 네이버 계정 및 비번
        s.sendmail(send_email, recv_email, msg.as_string())

    except Exception as e:
        print(f'예외 {e}')
    finally:
        if s is not None:
            s.close()


if __name__ == '__main__':
    name = '주양'
    receive_email = 'sidd45454@gmail.com'
    p_title = '테스트 메일'
    p_contents = '내용'
    # naver_smtp(name, receive_email, p_title, p_contents)

    mail_list = read_addressbook()

    print('---main---', mail_list)

    # 필요 없는 행 있을 경우 slice
    # for m_data in mail_list[1:]  -> 첫 줄 건너뛰기
    for m_data in mail_list:
        # print('m_data: '.format(m_data))
        list_str = m_data.split(";")
        # print(list_str)
        naver_smtp(name=list_str[0], receive_email=list_str[1], p_title=list_str[2], p_contents=list_str[3])

