import unittest
import pandas as pd
import numpy as np
from mtbp3.statlab.corr import CorrCalculator
import matplotlib.pyplot as plt

class TestCorrCalculator(unittest.TestCase):

    def setUp(self):
        self.y_df = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [2, 4, 6, 8, 10]})
        self.y_list = [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10]]
        self.corr_calculator_df = CorrCalculator(self.y_df)
        self.corr_calculator_list = CorrCalculator(self.y_list)

    def test_calculate_kendall_tau_with_dataframe(self):
        expected_tau = 1.0
        tau = self.corr_calculator_df.calculate_kendall_tau()
        self.assertEqual(tau, expected_tau)

    def test_calculate_kendall_tau_with_list(self):
        expected_tau = 1.0
        tau = self.corr_calculator_list.calculate_kendall_tau()
        self.assertEqual(tau, expected_tau)

    def test_plot_y_list(self):
        self.corr_calculator_df.plot_y_list()
        # No assertion, just checking if the plot is displayed correctly

if __name__ == "__main__":
    unittest.main()