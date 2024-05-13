import unittest
import  xzs_login

class MyTest(unittest.TestCase):
    xzs = xzs//*_login.login()
    def test_login_01(self):
        t =self.xzs.login("student","123456")
        self.assertIn("成功",t.text)


    def test_login_02(self):
        t=self.xzs.login("student","")
        self.assertIn("用户名或者密码错误",t.text)


if __name__== '__main--':
    unittest.main()
    def tearDOwnClass(cls):
        print(tearDOwnClass())

    def setUp(self):
        print("setUp")

    def tearDown(self):
        print(tearDown())
    def test_01(self):
        print("test01")

        self.assertEqual(True, True)
    def test_02(self):
        print("test02")
        self.assertEqual("h","hello")
    def test_03(self):
        print("test03")

        self.assertIsNot(1,1/1)
    def test_04(self):
        print("test04")

        self.assertLess(3,4)

    def test_05(self):
        print("test05")
        self.assertInstance({"user":"su","ps":123},dict)

if __name__=='__main__':
    unittest.main()






