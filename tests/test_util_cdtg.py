import unittest
import warnings
from mtbp3.util.cdtg import catPlotter
import pandas as pd

class TestCatPlotter(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            'Group': ['A', 'A', 'B', 'B', 'C', 'C'],
            'Value': [1, 2, 3, 4, 5, 6],
            'Grid': ['G1', 'G1', 'G2', 'G2', 'G1', 'G1'],
            'CValue': ['C1', 'C2', 'C1', 'C2', 'C1', 'C2'],
            'CValueGroup': [1, 1, 2, 2, 1, 1]
        })

    def test_boxplot(self):
        warnings.filterwarnings("ignore")
        plotter = catPlotter(self.df, y_col='Value', group_col='Group', x_col='CValue', grid_col='Grid')
        plotter.boxplot()

    def test_lineplot(self):
        plotter = catPlotter(self.df, y_col='Value', group_col='Group', x_col='CValue', grid_col='Grid')
        plotter.lineplot()

    def test_update_parameters(self):
        plotter = catPlotter(self.df, y_col='Value', group_col='Group', x_col='CValue', grid_col='Grid')
        plotter.update_parameters(y_col='NewValue', fig_size_0=10)
        self.assertEqual(plotter.y_col, 'NewValue')
        self.assertEqual(plotter.fig_size_0, 10)

if __name__ == "__main__":
    unittest.main()