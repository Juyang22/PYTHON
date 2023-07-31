'''
파일명: work_div.py
생성자: PCWK
생성일: 2023-07-27
'''

from abc import *

''' DAO 표준 '''
class WorkDiv(metaclass=ABCMeta):

    ''' 등록 '''
    @abstractmethod
    def do_save(self):
        pass

    ''' 삭제 '''
    @abstractmethod
    def do_delete(self):
        pass

    ''' 단건 조회 '''
    @abstractmethod
    def do_select_one(self):
        pass

    ''' 수정 '''
    @abstractmethod
    def do_update(self):
        pass

    ''' 목록 조회 '''
    @abstractmethod
    def do_retrieve(self):
        pass

