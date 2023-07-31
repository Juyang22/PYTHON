import unittest  # python junit : 파이썬 테스트 자동화 프레임워크


def add(a, b):
    return a + b

"""
1. unittest.TestCase 상속받기
2. 테스트 함수는 이름을 "test_"로 시작해야 함
3. 단정문 "assertXXX()" 결과 비교
4. setUp : 메서드 실행 전에 수행
5. 
"""


class TestAddFunc(unittest.TestCase):

    def setUp(self):
        print('-' * 50)
        print('-setUp()-')
        print('-' * 50)

    def test_add_positive(self):
        result = add(12, 14)
        print('test_add_positive result : {0}'.format(result))
        self.assertEqual(result, 26)

    def test_add_negative(self):
        result = add(-2, -4)
        print('test_add_negative result : {0}'.format(result))
        self.assertEqual(result, -6)


# run test
if __name__ == '__main__':
    unittest.main()
