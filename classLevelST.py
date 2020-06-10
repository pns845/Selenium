import unittest

class testCase2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("i will execute only once at the start")
    def test_case1(self):
        print("demo 1")
    def test_case2(self):
        print("demo 2")
    @classmethod
    def tearDownClass(cls):
        print("i will execute always at the end ")
if __name__ == '__main__':
    unittest.main(verbosity=2)
