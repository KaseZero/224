import os
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from config import *
from send_email import send_email

class MyTestCase(unittest.TestCase):
    def test_all(self):
        logging.info("============运行所有的case========")
        suit = unittest.defaultTestLoader.discover(test_path,'test*.py')
        # t = time.strftime('%Y_%m_%d_%H_%M_%S')
        with open(report_file, 'wb') as f:
            HTMLTestRunner(
                stream=f,
                title="xzs测试用例",
                description='xzs登录和注册用例集',
                verbosity=2
            ).run(suit)

        send_email(report_file)
        logging.info("============测试结束=============")

if __name__ == '__main__':
    unittest.main()
