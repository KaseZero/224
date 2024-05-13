import unittest
class Test1(unittest.TestCase):
    def setUp(self):
        print('Test1')

    def tearDown(self):
        print('Test1')

    def test_001(self):
        print('测试test! $$$$$')

class Test2(unittest.TestCase):
     def setUp(self):
         print('Test2')

    def tearDown(self):
        print('Test2')

     def test_001(self):
         print('测试test2 #####')

if __name__ == '__main__':
    if __name__ == '__main__':
        unittest()
