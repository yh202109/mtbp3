import unittest
from mtbp3.statlab.kappa import KappaCalculator
import statsmodels.stats.inter_rater as ir

class TestKappaCalculator(unittest.TestCase):

    def setUp(self):
        y1 = ['B'] * 70 + ['A'] * 30
        y2 = ['A'] * 70 + ['B'] * 30
        y3 = ['A'] * 50 + ['B'] * 30 + ['C'] * 20
        y4 = ['B'] * 40 + ['C'] * 40 + ['A'] * 20
        y5 = ['C'] * 60 + ['A'] * 20 + ['B'] * 20
        data = [y1, y2, y3, y4, y5]
        self.c1 = KappaCalculator([y1, y2])
        self.c2 = KappaCalculator(data)

    def test_cohen(self):
        gt0 = ir.cohens_kappa(self.c1.y_count_sq)
        self.assertAlmostEqual(gt0.kappa, self.c1.cohen_kappa, places=6)
        self.assertIsInstance(self.c1.cohen_kappa, float)
        self.assertGreaterEqual(self.c1.cohen_kappa, -1)
        self.assertLessEqual(self.c1.cohen_kappa, 1)

    def test_bootstrap_cohen_ci(self):
        result = self.c1.bootstrap_cohen_ci(n_iterations=1000, confidence_level=0.95, out_digits=6)
        self.assertIsInstance(result, str)
        self.assertIn("Cohen's kappa:", result)
        self.assertIn("Confidence Interval", result)

    def test_fleiss_kappa(self):
        gt1 = ir.fleiss_kappa(self.c1.y_count)
        gt2 = ir.fleiss_kappa(self.c2.y_count)
        self.assertAlmostEqual(gt1, self.c1.fleiss_kappa, places=6)
        self.assertAlmostEqual(gt2, self.c2.fleiss_kappa, places=6)
        self.assertIsInstance(gt2, float)
        self.assertGreaterEqual(gt2, -1)
        self.assertLessEqual(gt2, 1)

if __name__ == "__main__":
    unittest.main()