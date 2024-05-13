import unittest
from business.login import Login
class loginCase(unittest.TestCase):
    l=Login('Firefox')
    def test_liok(self):
        title=self.l.login('admin','Qwe123')
        self.assertEqual(title,'地盘')
if __name__=='__main__':
    unittest.main()