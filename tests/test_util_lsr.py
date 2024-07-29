import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
import unittest
from mtbp3 import util
import os


class TestLsrTree(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestLsrTree, self).__init__(*args, **kwargs)
        self.test_folder = util.get_data('test_lsr')

    def test_list_files_list(self):
        lsrt = util.lsr.LsrTree(self.test_folder, outfmt="list")
        files = lsrt.list_files()
        expected_files = ['/testfolder1/testfile10', '/testfolder1/testfile11', '/testfolder1/testfile12', '/testfolder2/testfile20', '/testfolder2/testfile3']
        self.assertCountEqual(files, expected_files)

    def test_list_files_json(self):
        lsrt = util.lsr.LsrTree(self.test_folder, outfmt="json")
        files = lsrt.list_files()
        expected_files = '{"0": {"path": "", "level": 0, "folders": ["testfolder1", "testfolder2"], "files": []}, "1": {"path": "/testfolder1", "level": 1, "folders": [], "files": ["testfile10", "testfile11", "testfile12"]}, "2": {"path": "/testfolder2", "level": 1, "folders": [], "files": ["testfile20", "testfile3"]}}'
        self.assertCountEqual(files, expected_files)

    def test_list_files_dataframe(self):
        lsrt = util.lsr.LsrTree(self.test_folder, outfmt="dataframe")
        files = lsrt.list_files()['file'].tolist()
        expected_files = ['testfile10', 'testfile11', 'testfile12', 'testfile20', 'testfile3']
        self.assertCountEqual(files, expected_files)

    def test_list_files_string(self):
        lsrt = util.lsr.LsrTree(os.path.join(self.test_folder, 'testfolder1'), outfmt="string")
        files = lsrt.list_files()
        expected_files = 'testfolder1/\n... testfile10\n... testfile11\n... testfile12'
        self.assertEqual(files, expected_files)

    def test_list_files_tree(self):
        #lsrt = lsr.LsrTree(os.path.join(self.test_folder, 'testfolder2'), outfmt="tree")
        lsrt = util.lsr.LsrTree(self.test_folder, outfmt="tree")
        files = lsrt.list_files()
        expected_files = 'test_lsr/\n├── testfolder1/\n│   ├── testfile10\n│   ├── testfile11\n│   └── testfile12\n└── testfolder2/\n    ├── testfile20\n    └── testfile3'
        self.assertEqual(files, expected_files)

    def test_list_files_tree2(self):
        lsrt = util.lsr.LsrTree(os.path.join(self.test_folder, 'testfolder2'), outfmt="tree", with_counts=True)
        files = lsrt.list_files()
        expected_files = 'testfolder2/  <<<((( F=2; D=0 )))>>>\n├── testfile20\n└── testfile3'
        self.assertEqual(files, expected_files)

if __name__ == "__main__":
    unittest.main()