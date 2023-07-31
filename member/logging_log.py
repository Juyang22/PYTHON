'''
Python의 logging 기능을 제공하는 내장 모듈로,
콘솔 로그, 파일 로그 기록 가능
프로그램 실행 중 발생하는 정보, 경고, 오류 등을 기록 가능
log level : DEBUT > INFO > WARNING > ERROR > CRITICAL
'''


# logging 모듈 가져오기
import logging

# asctime  : 로그 기록 시간
# lineno   : 라인 번호
# functoin : 함수 이름
# message  : 메시지

# formatter = logging.Formatter('%(asctime)s [%(filename)s:%(lineno)s|%(levelname)s] %(funcName)s(): %(message)s')
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(filename)s:%(lineno)s|%(levelname)s] %(funcName)s(): %(message)s')  # output level
log = logging.getLogger(__name__)

if __name__ == '__main__':
    log.critical('critical')
    log.error('error')
    log.warning('warning')
    log.info('info')
    log.debug('debug')
