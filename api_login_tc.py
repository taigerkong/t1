import unittest
from po.LoginAPI import LoginClass


class TestLoginAPI(unittest.TestCase):
    '''测试登录接口'''

    def setUp(self):
        self.l = LoginClass()

    def test_login_success_001(self):
        r = self.l.loginApi('13612345555', 'sf123456')
        self.assertEqual(r, '用户登陆成功')


if __name__ == '__main__':
    unittest.main()
