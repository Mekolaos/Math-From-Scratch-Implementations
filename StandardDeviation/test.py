import unittest
from StandardDeviation import mean, variance, standard_deviation

class MathTest(unittest.TestCase):

    def setUp(self):
        self.num_array = [600, 470, 170, 430, 300]
        self.real_data_len = len(self.num_array)
        self.sample_data_len = len(self.num_array)-1
    
    def test_mean(self):
        self.assertEqual(mean(self.num_array), 394)
    
    def test_variance(self):
        # Real data case
        self.assertEqual(variance(self.num_array, self.real_data_len), 21704)
        # Sample data case
        self.assertEqual(variance(self.num_array, self.sample_data_len), 27130)


    def test_standard_deviation(self):
        # Real data case
        self.assertEqual(standard_deviation(self.num_array, False), 147)
        # Sample data case 
        self.assertEqual(standard_deviation(self.num_array, True), 164)