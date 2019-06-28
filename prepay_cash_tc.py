import unittest
from po.MyP2P.PrepayCashAPI import PrepayClass


class TestPrepayAPI(unittest.TestCase):
    '''测试线下充值接口'''

    def setUp(self):
        self.p = PrepayClass()

    def test_login_success_001(self):
        r = self.p.prepayApi()
        self.assertEqual(r, '充值成功')


if __name__ == '__main__':
    unittest.main()
