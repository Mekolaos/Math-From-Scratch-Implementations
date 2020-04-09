import unittest
from StandardDeviation import mean, variance, standard_deviation

class MathTest(unittest.TestCase):

    def setUp(self):
        self.num_array = [600, 470, 170, 430, 300]
    
    def test_mean(self):
        self.assertEqual(mean(self.num_array), 394)
    
    def test_variance(self):
        self.assertEqual(variance(self.num_array), 21704)

    def test_standard_deviation(self):
        self.assertEqual(standard_deviation(self.num_array), 147)