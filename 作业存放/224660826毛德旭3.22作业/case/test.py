import unittest
from business.login import Login
class loginCase(unittest.TestCase):
    l=Login('Firefox')
    def test_liok(self):
        title=self.l.login('admin','Abc123456','0')
        self.assertEqual(title,'我的地盘 - 禅道')
    def test_opli(self):
        tit=self.l.login('','','1')
        self.assertEqual(tit,'登录失败，请检查您的用户名或密码是否填写正确。')
if __name__=='__main__':
    unittest.main()
    