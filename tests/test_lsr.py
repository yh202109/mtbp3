import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
import unittest
from mtbp3.util.lsr import LsrTree
import mtbp3
import os


class TestLsrTree(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestLsrTree, self).__init__(*args, **kwargs)
        self.test_folder = mtbp3.get_data('test_lsr')

    def test_list_files_list(self):
        lsr = LsrTree(self.test_folder, outfmt="list")
        files = lsr.list_files()
        expected_files = ['/testfolder1/testfile11', '/testfolder2/testfile20', '/testfolder2/testfile3']
        self.assertCountEqual(files, expected_files)

    def test_list_files_json(self):
        lsr = LsrTree(self.test_folder, outfmt="json")
        files = lsr.list_files()
        expected_files = '{"0": {"path": "", "level": 0, "folders": ["testfolder1", "testfolder2"], "files": []}, "1": {"path": "/testfolder1", "level": 1, "folders": [], "files": ["testfile11"]}, "2": {"path": "/testfolder2", "level": 1, "folders": [], "files": ["testfile20", "testfile3"]}}'
        self.assertCountEqual(files, expected_files)

    def test_list_files_dataframe(self):
        lsr = LsrTree(self.test_folder, outfmt="dataframe")
        files = lsr.list_files()['file'].tolist()
        expected_files = ['testfile11', 'testfile20', 'testfile3']
        self.assertCountEqual(files, expected_files)

    def test_list_files_string(self):
        lsr = LsrTree(os.path.join(self.test_folder, 'testfolder1'), outfmt="string")
        files = lsr.list_files()
        expected_files = 'testfolder1/\n... testfile11'
        self.assertEqual(files, expected_files)

    def test_list_files_tree(self):
        #lsr = LsrTree(os.path.join(self.test_folder, 'testfolder2'), outfmt="tree")
        lsr = LsrTree(self.test_folder, outfmt="tree")
        files = lsr.list_files()
        expected_files = 'test_lsr/\n├── testfolder1/\n│   └── testfile11\n└── testfolder2/\n    ├── testfile20\n    └── testfile3'
        self.assertEqual(files, expected_files)

    def test_list_files_tree2(self):
        lsr = LsrTree(os.path.join(self.test_folder, 'testfolder2'), outfmt="tree", with_counts=True)
        files = lsr.list_files()
        expected_files = 'testfolder2/  <<<((( F=2; D=0 )))>>>\n├── testfile20\n└── testfile3'
        self.assertEqual(files, expected_files)

if __name__ == "__main__":
    unittest.main()