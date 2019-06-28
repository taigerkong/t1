import unittest
from po.MyP2P.AddBankCardAPI import AddBankCardClass


class TestAddBankAPI(unittest.TestCase):
    '''测试线下充值接口'''

    def setUp(self):
        self.a = AddBankCardClass()

    def test_login_success_001(self):
        r = self.a.addBankCardApi()
        self.assertEqual(r, '银行卡添加成功')


if __name__ == '__main__':
    unittest.main()
