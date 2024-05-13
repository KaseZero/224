import unittest
from business.login import zentao

class loginCase(unittest.TestCase):
    l=zentao()
    def loginok(self):
        t = self.l.login('admin','Qwe123',0)
        self.assertEqual(t, '地盘 - 禅道')

    def text_loginerr001(self):
        t = self.l.login('admin','232',1)
        self.assertEqual(t,'登录失败，请检查您的用户名或密码是否填写正确。')

    def text_loginerr002(self):
        t = self.l.login('123','Qwe123',1)
        self.assertEqual(t,'登录失败，请检查您的用户名或密码是否填写正确。')

    def text_loginerr003(self):
        t = self.l.login('13', '131', 1)
        self.assertEqual(t, '登录失败，请检查您的用户名或密码是否填写正确。')

if __name__ == '__main__':
    unittest.main()
