import unittest
import pandas as pd
import mtbp3
from mtbp3.stdiso.pdfsummary import pdfSummary

class TestPdfSummary(unittest.TestCase):

    def setUp(self):
        self.pdf_summary = pdfSummary()

    def test_compare_file_size(self):
        expected_file_size = 2215244
        file_size = self.pdf_summary.summary['file_size']
        self.assertEqual(file_size, expected_file_size)

    def test_get_outline_list(self):
        expected_outline_list = [
            [
                'attention.pdf', 
                'attention.pdf.pseudo1-00 Introduction', 
                'attention.pdf.pseudo1-01 Background', 
                'attention.pdf.pseudo1-02 Model Architecture', 
                'attention.pdf.pseudo1-02.sub 5 sub-sections', 
                'attention.pdf.pseudo1-04 Why Self-Attention', 
                'attention.pdf.pseudo1-05 Training', 
                'attention.pdf.pseudo1-05.sub 4 sub-sections', 
                'attention.pdf.pseudo1-07 Results', 
                'attention.pdf.pseudo1-07.sub 3 sub-sections', 
                'attention.pdf.pseudo1-09 Conclusion'
            ],
            []
        ]

        outline_list = self.pdf_summary.get_outline_list(max_itr=1)
        self.assertEqual(outline_list, expected_outline_list)

    def test_show_outline_tree(self):
        expected_outline_tree = """    attention.pdf
    ├── Introduction
    ├── Background
    ├── Model Architecture
    │   └── 5 sub-sections
    ├── Why Self-Attention
    ├── Training
    │   └── 4 sub-sections
    ├── Results
    │   └── 3 sub-sections
    └── Conclusion"""
        outline_tree = self.pdf_summary.show_outline_tree(max_itr=1)
        self.assertEqual(outline_tree, expected_outline_tree)

if __name__ == "__main__":
    unittest.main()