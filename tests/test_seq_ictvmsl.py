import unittest
import os
import pandas as pd
from mtbp3.seq.ictvmslview import ictvmsl

class TestIctvmsl(unittest.TestCase):

    def setUp(self):
        self.valid_file_path = 'supp_seq/ICTV_MSL39v4_example.csv'
        self.invalid_file_path = 'invalid_path.csv'
        self.default_file_path = 'supp_seq/ICTV_MSL39v4_example.csv'

    def test_init_with_valid_file_path(self):
        obj = ictvmsl(self.valid_file_path)
        self.assertEqual(obj.msl_file_path, self.valid_file_path)
        self.assertTrue(isinstance(obj.msl, pd.DataFrame))

    def test_init_with_invalid_file_path(self):
        with self.assertRaises(FileNotFoundError):
            ictvmsl(self.invalid_file_path)

    def test_init_with_default_file_path(self):
        obj = ictvmsl()
        self.assertEqual(obj.msl_file_path, self.default_file_path)
        self.assertTrue(isinstance(obj.msl, pd.DataFrame))

    def test_init_with_non_string_file_path(self):
        with self.assertRaises(TypeError):
            ictvmsl(123)

if __name__ == "__main__":
    unittest.main()