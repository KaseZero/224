import unittest
import time
from business import fzt
class Testaddbug(unittest.TestCase):
    zt=fzt.zentao()
     # 影响版本和标题都正确
    def test_addbug_ok(self):
        self.zt.login('admin','Qwe123',0)
        t=self.zt.addbug(0,'标题',0)
        time.sleep(3)
        self.assertEqual(t,'保存成功')
        self.zt.logout()

    # 影响版本空  标题都正确
    def test_addbug_err01(self):
        self.zt.login('admin', 'Qwe123', 0)
        t = self.zt.addbug(1, '标题1', 1)
        self.assertEqual(t, '『影响版本』不能为空。')
        self.zt.logout()
    # 影响版本正确 标题为空
    def test_addbug_err02(self):
        self.zt.login('admin', 'Qwe123', 0)
        t = self.zt.addbug(0, '', 1)
        self.assertEqual(t, '标题不能为空 !')
        self.zt.logout()
    # 影响版本正确 标题超过长度限制
    def test_addbug_err03(self):
         self.zt.login('admin', 'Qwe123', 0)
         a1 = "a" * 300
         t = self.zt.addbug(0, a1, 1)
         self.assertEqual(t, '『Bug标题』长度应当不超过『255』，且大于『0』。')
         self.zt.logout()
    # 影响版本为空 标题为空
    def test_addbug_err04(self):
        self.zt.login('admin', 'Qwe123', 0)
        t = self.zt.addbug(0, '', 1)
        self.assertEqual(t, '标题不能为空 != 『Bug标题』不能为空。')
        self.zt.logout()
if __name__=='__main__':
    unittest.main()