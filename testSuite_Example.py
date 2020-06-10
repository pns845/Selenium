import unittest
from module25.assertExample import assertDemo
from module25.unitTest import sampleTest

#get all the tests from testclass

tc1 = unittest.TestLoader().loadTestsFromTestCase(sampleTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(assertDemo)
#create test suite combining 
final_test = unittest.TestSuite([tc1,tc2])
unittest.TextTestRunner(verbosity=2).run(final_test)