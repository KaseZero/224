import unittest
import arithmetic

class MyTestCase(unittest.TestCase):
    a =arithmetic.ari()
    def test_add_1(self):
        # 实际结果
        p =self.a.add(3,4)
        # 7是预期结果
        self.assertEqual(p, 7)
    def test_add_2(self):
        p=self.a.add(0.1,0.5)
        self.assertEqual(p,0.6)
    def test_add_3(self):
        p=self.a.add(0,1)
        self.assertEqual(p,1)
    def test_add_4(self):
        p=self.a.add(-1,-5)
        self.assertEqual(p,-6)


if __name__ == '__main__':
    unittest.main()
