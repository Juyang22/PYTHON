import unittest

from member_vo import MemberVO
from member_dao import MemberDao
from common.search import SearchDiv
import common.pcwk_logging as p_log


class TestMemberDao(unittest.TestCase):
    """ MemberDao CRUD 테스트 """
    def setUp(self):
        self.member_dao = MemberDao()
        self.m01 = MemberVO('pcwk_11_11', '이상뮤', '4321', 'sidd4545@gmail.com', '', 'pcwk')
        self.m02 = MemberVO('pcwk_11_12', '이상뮤', '4321', 'sidd4545@gmail.com', '', 'pcwk')
        self.m03 = MemberVO('pcwk_11_13', '이상뮤', '4321', 'sidd4545@gmail.com', '', 'pcwk')
        self.search10 = SearchDiv(search_div="10", search_word='이상무')
        self.search20 = SearchDiv(search_div="20", search_word='sidd4545')
        self.search30 = SearchDiv(search_div="30", search_word='pcwk_11')

    def test_do_retrieve(self):
        self.member_dao.do_retrieve(self.search30)

    def ctest_do_update(self):
        # 1. 삭제
        # 2. 등록
        # 3. 조회
        # 4. 수정
        # 5. 다시 조회
        # 6. 수정된 데이터 vs 조회 데이터 비교

        # 1.
        self.member_dao.do_delete(self.m01)
        self.member_dao.do_delete(self.m02)
        self.member_dao.do_delete(self.m03)

        # 2. 등록
        self.member_dao.do_save(self.m01)

        # 3. 조회
        mV01 = self.member_dao.do_select_one(self.m01)

        # 4. 수정
        up_str = '뮤'

        mV01.name = mV01.name + "" + up_str
        mV01.passwd = mV01.passwd + "" + up_str
        mV01.email = mV01.email + "" + up_str
        mV01.reg_id = mV01.reg_id + "" + up_str

        self.member_dao.do_update(mV01)

        # 5. 다시 조회
        mVS01 = self.member_dao.do_select_one(mV01)

        # 6. 비교
        self.is_same_data(mV01, mVS01)

        # flag = self.member_dao.do_update(self.m01)
        # print('flag : {}'.format(flag))
        # self.assertEqual(flag, 1)


    ''' 삭제, 등록, 조회 '''
    def ctest_add_and_get(self):
        # 삭제
        self.member_dao.do_delete(self.m01)
        self.member_dao.do_delete(self.m02)
        self.member_dao.do_delete(self.m03)

        # 등록
        self.member_dao.do_save(self.m01)
        self.member_dao.do_save(self.m02)
        self.member_dao.do_save(self.m03)

        # 조회
        vs1 = self.member_dao.do_select_one(self.m01)
        vs2 = self.member_dao.do_select_one(self.m02)
        vs3 = self.member_dao.do_select_one(self.m03)

        # 비교
        self.is_same_data(vs1, self.m01)
        self.is_same_data(vs2, self.m02)
        self.is_same_data(vs3, self.m03)

    def ctest_do_select_one(self):
        outVO01 = self.member_dao.do_select_one(self.m01)
        p_log.logger2.debug('outVO1 : {}'.format(outVO01))
        self.assertIsNotNone(outVO01)
        self.is_same_data(outVO01, self.m01)

    def ctest_do_delete(self):
        flag = self.member_dao.do_delete(self.m01)
        p_log.logger2.debug('flag : {}'.format(flag))

    def ctest_do_save(self):
        flag = self.member_dao.do_save(self.m01)
        p_log.logger2.debug('flag : {}'.format(flag))
        self.assertEqual(flag, 1)

    def is_same_data(self, org:MemberVO, vs:MemberVO):
        self.assertEqual(org.user_id, vs.user_id)
        self.assertEqual(org.name, vs.name)
        self.assertEqual(org.passwd, vs.passwd)
        self.assertEqual(org.email, vs.email)
        self.assertEqual(org.reg_id, vs.reg_id)


if __name__ == '__main__':
    unittest.main()

