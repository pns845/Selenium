import unittest
#
# class Testing(unittest.TestCase):
#     def test_1(self):
#         x=1
#         self.assertEqual(x,1)
#
#     def test_hello_world(self):
#         self.text = 'hello World'
#         text_req = self.text.lower()
#         self.assertEqual(text_req,'hello world')

class sampleTest(unittest.TestCase):
    def setUp(self):
        print("this is exeuted before")
    def testA(self):
        print("A os printed")
    def testB(self):
        print("B is printed")
    def tearDown(self):
        print("this is executed after")

if __name__ == '__main__':
    unittest.main(verbosity=2)


