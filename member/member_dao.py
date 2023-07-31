import oracledb
import common.pcwk_logging as p_log
from common.work_div import WorkDiv
from common.search import SearchDiv
from member_vo import MemberVO
import logging

"""
        flag = 0
        try:
            pass
        except oracledb.DatabaseError as e:
            print('DatabaseError:{}'.format(e))
        except Exception as e:
            print('Exception:{}'.format(e))
        finally:
            print('6. finally')
            self.disconnect_db()
        return flag
"""


class MemberDao(WorkDiv):
    # 생성자
    def __init__(self):
        # DB Connection 변수
        self.conn = None

    """ DB 연결 """
    def connect_db(self):
        try:
            # 'host:port/service_name'
            self.conn = oracledb.connect(user='scott', password='pcwk', dsn='192.168.0.123:1521/XE')  # DB Connection
            p_log.logger2.debug(self.conn)
        except oracledb.DatabaseError as e:
            p_log.logger2.debug('DatabaseError:{}'.format(e))
        except Exception as e:
            p_log.logger2.debug('-' * 50)
            p_log.logger2.debug('connect_db : {}'.format(e))
            p_log.logger2.debug('-' * 50)

    """ DB 자원 반납 """
    def disconnect_db(self):
        try:
            if self.conn is not None:
                self.conn.close()
        except oracledb.DatabaseError as e:
            p_log.logger2.debug('DatabaseError:{}'.format(e))
        except Exception as e:
            p_log.logger2.debug('-' * 50)
            p_log.logger2.debug('disconnect_db : {}'.format(e))
            p_log.logger2.debug('-' * 50)

    def do_save(self, member: MemberVO):  # param: type
        flag = 0
        try:
            """
            1. DB 연결
            2. param 확인
            3. cursor 생성
            4. SQL 정의
            5. SQL 실행
            6. 트랜잭션 처리
            7. 자원 반납
            """

            # 1.
            self.connect_db()
            p_log.logger2.debug('1. self.conn : {0}'.format(self.conn))

            # 2.
            p_log.logger2.debug('2. param : {0}'.format(member))

            # 3.
            cur = self.conn.cursor()
            p_log.logger2.debug('3. cur : {0}'.format(cur))

            # 4.
            sql = '''
            INSERT INTO member (
                user_id,
                name,
                pass,
                email,
                reg_dt,
                reg_id
            ) VALUES (
                :1,
                :2,
                :3,
                :4,
                sysdate,
                :5
            )
            '''
            p_log.logger2.debug('4. sql : {}'.format(sql))

            # 5.
            cur.execute(sql, (member.user_id,
                            member.name,
                            member.passwd,
                            member.email,
                            member.reg_id))

            # 6.
            self.conn.commit()
            flag = cur.rowcount  # 반영된 건수
            p_log.logger2.debug('5. flag : {}'.format(flag))

        except oracledb.DatabaseError as e:
            p_log.logger2.debug('oracledb.DatabaseError : {}'.format(e))

        except Exception as e:
            p_log.logger2.debug('Exception : {}'.format(e))

        finally:
            p_log.logger2.debug('6. finally')
            self.disconnect_db()

        return flag

    def do_delete(self, member:MemberVO):
        flag = 0
        try:
            """
            1. DB 연결
            2. param 확인
            3. cursor 생성
            4. SQL 정의
            5. SQL 실행
            6. 트랜잭션 처리
            7. 자원 반납
            """

            # 1.
            self.connect_db()
            p_log.logger2.debug('1. self.conn : {}'.format(self.conn))

            # 2.
            p_log.logger2.debug('2. member : {}'.format(member))

            # 3.
            cur = self.conn.cursor()
            p_log.logger2.debug('3. cur : {}'.format(cur))

            # 4.
            sql = 'DELETE FROM member WHERE user_id = :1'
            p_log.logger2.debug('4. sql : {}'.format(sql))

            # 5.
            cur.execute(sql, (member.user_id,))  # 튜플에 data 1개일 때 끝에 ',' 찍어야 함

            # 6.
            self.conn.commit()
            flag = cur.rowcount  # 반영 건수
            p_log.logger2.debug('5. flag : {}'.format(flag))

        except oracledb.DatabaseError as e:
            p_log.logger2.debug('oracledb.DatabaseError : {}'.format(e))

        except Exception as e:
            p_log.logger2.debug('Exception : {}'.format(e))

        finally:
            p_log.logger2.debug('6. finally')
            self.disconnect_db()

        return flag

    def do_select_one(self, member:MemberVO):
        outVO = None  # list data
        vo    = None  # return data(MemberVO)
        sql = '''
                SELECT 
                    user_id,
                    name,
                    pass,
                    email,
                    TO_CHAR(reg_dt, 'YYYY-MM-DD HH24:MI:SS') reg_dt,
                    reg_id
                FROM
                    member
                WHERE user_id = :1
                '''

        try:
            """
            1. DB 연결
            2. param 확인
            3. cursor 생성
            4. SQL 정의
            5. SQL 실행
            6. 트랜잭션 처리
            7. 자원 반납
            """

            self.connect_db()  # 1.
            p_log.logger2.debug('1. self.conn : {}'.format(self.conn))
            p_log.logger2.debug('2. member : {}'.format(member))

            cur = self.conn.cursor()
            p_log.logger2.debug('3. cur : {}'.format(cur))
            p_log.logger2.debug('4. sql : {}'.format(sql))

            cur.execute(sql, (member.user_id,))  # tuple은 데이터가 1개인 경우 ',' 붙여야 함!

            # 리스트 내포 : 데이터 조회
            outVO = [MemberVO(user_id=row[0],
                            name=row[1],
                            passwd=row[2],
                            email=row[3],
                            reg_dt=row[4],
                            reg_id=row[5]
                        ) for row in cur]

            if None != outVO and len(outVO) > 0:
                vo = outVO[0]
                p_log.logger2.debug('vo : {}, {}, {}, {}, {}, {}'.format(vo.user_id,
                                                                        vo.name,
                                                                        vo.passwd,
                                                                        vo.email,
                                                                        vo.reg_dt,
                                                                        vo.reg_id))

        except oracledb.DatabaseError as e:
            p_log.logger2.debug('oracledb.DatabaseError : {}'.format(e))

        except Exception as e:
            p_log.logger2.debug('Exception : {}'.format(e))

        finally:
            p_log.logger2.debug('6. finally')
            self.disconnect_db()

        return vo

    def do_update(self, member:MemberVO):
        flag = 0
        try:
            """
            1. DB 연결
            2. param 확인
            3. cursor 생성
            4. SQL 정의
            5. SQL 실행
            6. 트랜잭션 처리
            7. 자원 반납
            """

            # 1.
            self.connect_db()
            p_log.logger2.debug('1. self.conn : {}'.format(self.conn))

            # 2.
            p_log.logger2.debug('2. param : {}'.format(member))

            # 3.
            cur = self.conn.cursor()
            p_log.logger2.debug('3. cur : {0}'.format(cur))

            # 4.
            sql = '''
                    UPDATE member
                    SET name = :1,
                        pass = :2,
                        email = :3,
                        reg_dt = SYSDATE,
                        reg_id = :4
                    WHERE 
                        user_id = :5
                    '''
            p_log.logger2.debug('4. sql : {}'.format(sql))

            # 5.
            cur.execute(sql, (member.name,
                            member.passwd,
                            member.email,
                            member.reg_id,
                            member.user_id))

            # 6.
            self.conn.commit()
            flag = cur.rowcount  # 반영 건수
            p_log.logger2.debug('5. flag : {}'.format(flag))

        except oracledb.DatabaseError as e:
            p_log.logger2.debug('oracledb.DatabaseError : {}'.format(e))

        except Exception as e:
            p_log.logger2.debug('Exception : {}'.format(e))

        finally:
            p_log.logger2.debug('6. finally')
            self.disconnect_db()

        return flag

    def do_retrieve(self, search:SearchDiv):
        ''' 조회
            10 : 이름
            20 : email
            30 : user_id
        '''
        sql_where = ''
        sql_where_total = ''

        if "10" == search.search_div:
            sql_where       = 'AND name LIKE :1 \n'
            sql_where_total = 'AND name LIKE :2 \n'
        elif "20" == search.search_div:
            sql_where       = 'AND email LIKE :1 \n'
            sql_where_total = 'AND email LIKE :2 \n'
        elif "30" == search.search_div:
            sql_where       = 'AND user_id LIKE :1 \n'
            sql_where_total = 'AND user_id LIKE :2 \n'

        sql = ""
        sql += " SELECT A.*, B.*                                                                                  \n "
        sql += " FROM (                                                                                           \n "
        sql += "     SELECT tt1.rnum num,                                                                         \n "
        sql += "             tt1.user_id,  -- 여기서 주면 10건에 대해서만, 아래에서 주면 전체 건수에 적용               \n "
        sql += "             tt1.name,                                                                            \n "
        sql += "             tt1.pass,                                                                            \n "
        sql += "             tt1.email,                                                                           \n "
        sql += "             -- 당일이면: HH24:MI                                                                  \n "
        sql += "             -- 그렇지 않으면: YYYY-MM-DD                                                           \n "
        sql += "             DECODE(TO_CHAR(tt1.reg_dt, 'YYYY/MM/DD'), TO_CHAR(SYSDATE, 'YYYY/MM/DD'),            \n "
        sql += "                                                         TO_CHAR(tt1.reg_dt, 'HH24:MI'),          \n "
        sql += "                                                         TO_CHAR(SYSDATE, 'YYYY/MM/DD')) reg_dt,  \n "
        sql += "             tt1.reg_id                                                                           \n "
        sql += "     FROM (                                                                                       \n "
        sql += "         SELECT ROWNUM AS rnum, t1.*                                                              \n "
        sql += "         FROM (                                                                                   \n "
        sql += "             SELECT *                                                                             \n "
        sql += "             FROM member                                                                          \n "
        sql += "             WHERE 1 = 1                                                                          \n "
        # 동적 SQL
        if "10" == search.search_div:
            sql += sql_where
        elif "20" == search.search_div:
            sql += sql_where
        elif "30" == search.search_div:
            sql += sql_where
        # 한 줄로 쓰면 if "" != search.search_div:
        sql += "             ORDER BY reg_dt DESC                                                                 \n "
        sql += "         ) t1                                                                                     \n "
        sql += "     WHERE ROWNUM <= 10                                                                           \n "
        sql += "     ) tt1                                                                                        \n "
        sql += " WHERE rnum >= 1                                                                                  \n "
        sql += " ) A                                                                                              \n "
        sql += " CROSS JOIN                                                                                       \n "
        sql += " (                                                                                                \n "
        sql += " -- 전체 글 수                                                                                     \n "
        sql += " SELECT COUNT(*) total_cnt                                                                        \n "
        sql += " FROM member                                                                                      \n "
        sql += " WHERE 1 = 1                                                                                      \n "
        if "10" == search.search_div:
            sql += sql_where_total
        elif "20" == search.search_div:
            sql += sql_where_total
        elif "30" == search.search_div:
            sql += sql_where_total
        sql += " ) B                                                                                              \n "

        outList = []

        try:
            """
            1. DB 연결
            2. param 확인
            3. cursor 생성
            4. SQL 정의
            5. SQL 실행
            6. 트랜잭션 처리
            7. 자원 반납
            """
            self.connect_db()  # 1.
            p_log.logger2.debug('1. self.conn : {}'.format(self.conn))
            # p_log.logger2.debug('2. member : {}'.format(member))  # 2.

            cur = self.conn.cursor()  # 3.
            p_log.logger2.debug('3. cur : {}'.format(cur))
            p_log.logger2.debug('4. sql : {}'.format(sql))  # 4.

            if "" != search.search_div:  # 검색 조건이 있으면
                cur.execute(sql, (search.search_word+'%', search.search_word+'%'))
            else:   # 검색 조건이 없으면
                cur.execute(sql, )

            # 리스트 내포 : 데이터 조회
            outList = [MemberVO(num=row[0],
                                user_id=row[1],
                                name=row[2],
                                passwd=row[3],
                                email=row[4],
                                reg_dt=row[5],
                                reg_id=row[6],
                                total_cnt=row[7]
                            ) for row in cur]

            for vo in outList:
                p_log.logger2.debug('vo : {}'.format(vo))

        except oracledb.DatabaseError as e:
            p_log.logger2.debug('DatabaseError:{}'.format(e))

        except Exception as e:
            p_log.logger2.debug('Exception:{}'.format(e))

        finally:
            p_log.logger2.debug('6. finally')
            self.disconnect_db()

        return outList


if __name__ == '__main__':
    m01 = MemberVO('pcwk', '이상뮤', '4321', 'sidd4545@gmail.com', '', 'pcwk')
    dao = MemberDao()
    dao.do_save(m01)
