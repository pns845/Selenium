import unittest

class assertDemo(unittest.TestCase):
    def test_Case1(self):
        a = True
        self.assertTrue(a , "a is not True")
    def test_assertCompare(self):
        b = 10
        c = 10
        self.assertEqual(b,c,msg="c and b are not equal")
    def test_assertgreater(self):
        d=1000
        g=5000
        self.assertGreater(g,d, msg='g is greater')

if __name__ == '__main__':
    unittest.main(verbosity=2)