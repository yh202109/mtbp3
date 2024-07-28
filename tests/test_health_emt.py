import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import unittest
import pandas as pd
from mtbp3.health import emt

class TestEmt(unittest.TestCase):

    def setUp(self):
        self.emt = emt.Emt()
        self.emt.find_files()

    def test_expected_file_lists(self):
        support_doc_files, med_ascii_files, seq_ascii_files = self.emt.expected_file_lists()
        self.assertEqual(len(support_doc_files), 8)
        self.assertEqual(len(med_ascii_files), 14)
        self.assertEqual(len(seq_ascii_files), 10)

    def test_find_files(self):
        missing_files, message = self.emt.find_files()
        self.assertEqual(len(missing_files), 0)
        self.assertTrue("All files found" in message)

    def test_list_files(self):
        files = self.emt.list_files()
        first_file = files.split('\n')[0] 
        self.assertEqual(first_file, "MedDRA/  <<<((( F=8; D=2 )))>>>")

    def test_find_soc(self):
        soc_names = self.emt.find_soc()
        self.assertIsNotNone(soc_names)
        self.assertIsInstance(soc_names, list)
        self.assertGreater(len(soc_names), 0)

    def test_find_hlgt(self):
        hlgt_names = self.emt.find_hlgt()
        self.assertIsNotNone(hlgt_names)
        self.assertIsInstance(hlgt_names, list)
        self.assertGreater(len(hlgt_names), 0)

    def test_find_hlt(self):
        hlt_names = self.emt.find_hlt()
        self.assertIsNotNone(hlt_names)
        self.assertIsInstance(hlt_names, list)
        self.assertGreater(len(hlt_names), 0)

    def test_find_pt(self):
        pt_names = self.emt.find_pt()
        self.assertIsNotNone(pt_names)
        self.assertIsInstance(pt_names, list)
        self.assertGreater(len(pt_names), 0)

    def test_find_llt(self):
        llt_names = self.emt.find_llt()
        self.assertIsNotNone(llt_names)
        self.assertIsInstance(llt_names, list)
        self.assertGreater(len(llt_names), 0)

    def test_find_pt_given_soc(self):
        soc_names = self.emt.find_soc()
        soc_name = soc_names[0]
        df = self.emt.find_pt_given_soc(soc_name)
        self.assertIsNotNone(df)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertGreater(len(df), 0)
        self.assertEqual(df.columns.tolist(), ['pt_id', 'pt', 'soc_id', 'soc', 'primary'])

    def test_find_pt_given_soc_primary_only(self):
        soc_names = self.emt.find_soc()
        soc_name = soc_names[0]
        df = self.emt.find_pt_given_soc(soc_name, primary_soc_only=True)
        self.assertIsNotNone(df)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertGreater(len(df), 0)
        self.assertEqual(df.columns.tolist(), ['pt_id', 'pt', 'soc_id', 'soc'])

if __name__ == "__main__":
    unittest.main()