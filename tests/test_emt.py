import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import unittest
from mtbp3.util.emt import Emt

class TestEmt(unittest.TestCase):
    def setUp(self):
        self.emt = Emt()

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

    def test_find_pt_given_soc(self):
        soc_names = self.emt.find_soc()
        soc_name = soc_names[0]
        df = self.emt.find_pt_given_soc(soc_name)
        self.assertIsNotNone(df)
        self.assertEqual(len(df), 31)
        self.assertEqual(df.columns.tolist(), ['Id', 'Name', 'Primary'])

    def test_find_pt_given_soc_primary_only(self):
        soc_names = self.emt.find_soc()
        soc_name = soc_names[0]
        df = self.emt.find_pt_given_soc(soc_name, primary_soc_only=True)
        self.assertIsNotNone(df)
        self.assertEqual(len(df), 27)
        self.assertEqual(df.columns.tolist(), ['Id', 'Name'])

if __name__ == "__main__":
    unittest.main()