'''
파일명: member_vo.py
생성자: PCWK
생성일: 2023-07-27
'''
from common.dto import DTO


class MemberVO(DTO):

    # 생성자
    def __init__(self, user_id, name, passwd, email, reg_dt=None, reg_id=None, num=0, total_cnt=0):
        super().__init__(num, total_cnt)   # DTO의 num, total_cnt 호출

        self.user_id = user_id  # 아이디
        self.name = name        # 이름
        self.passwd = passwd    # 비밀번호
        self.email = email      # 이메일
        self.reg_dt = reg_dt    # 등록일
        self.reg_id = reg_id    # 등록명

    # 인스턴스 변수들을 문자열로 변환
    def __str__(self):
        return 'user_id : {0}, name : {1}, passwd : {2}, email : {3}, reg_dt : {4}, reg_id : {5}, num : {6},' \
               ' total_cnt : {7}'.format(self.user_id, self.name, self.passwd, self.email, self.reg_dt, self.reg_id,
                                        self.num, self.total_cnt)


if __name__ == '__main__':
    m01 = MemberVO('PCWK', '이상유', '4321', 'sidd4545@gmail.com', None, 'pcwk')
