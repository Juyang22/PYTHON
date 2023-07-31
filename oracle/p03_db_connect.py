'''
오라클 db 연결
'''
import oracledb


def main():
    ####################
    # DB 접속
    ####################
    con = oracledb.connect(user='scott', password='pcwk', dsn='192.168.0.123:1521/XE')  # DB Connection
    print('con', con)

    # SQL 수행
    cursor = con.cursor()  # 커서 생성
    sql = 'INSERT INTO test_tbl ( msg ) VALUES ( :1 )'
    param_data_one = 'haha'

    cursor.execute(sql, [param_data_one])  # 쿼리 수행

    # COMMIT
    con.commit()

    # 자원 반납
    con.close()


main()
