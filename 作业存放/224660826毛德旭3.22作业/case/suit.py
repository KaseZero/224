from common.HTMLTestRunner import HTMLTestRunner
from test import loginCase
import unittest
class SuitTest(unittest.TestCase):
    def test_suit(self):
        mysuit=unittest.TestSuite()
        mysuit.addTest(loginCase('test_liok'))
        mysuit.addTest(loginCase('test_opli'))
        with open('report.html','wb') as f:
            HTMLTestRunner(
                stream=f,
                title='测试报告',
                description='测试报告',
                verbosity=2
            ).run(mysuit)
if __name__=='__main__':
    unittest.main()