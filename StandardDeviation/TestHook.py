import unittest
from test import *

def Suite():
    suite = unittest.TestSuite()
    suite.addTest(MathTest('test_mean'))
    suite.addTest(MathTest('test_variance'))
    suite.addTest(MathTest('test_standard_deviation'))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(Suite())