import unittest
from mtbp3.health import ectd

class TestCtocByFDA(unittest.TestCase):

    def setUp(self):
        self.ctoc = ectd.ctoc_by_fda(ectd_version="3.2.2", ctoc_version="2.3.3")

    def test_load_list(self):
        self.assertIsInstance(self.ctoc.ctoc, list)
        self.assertGreater(len(self.ctoc.ctoc), 0)

    def test_show_ctoc_tree(self):
        tree = self.ctoc.show_ctoc_tree(module=1, to_right=False)
        self.assertIsInstance(tree[0], str)
        self.assertGreater(len(tree), 0)

    def test_find_section_given_words(self):
        result = self.ctoc.find_section_given_words("REMS", outfmt='simple', include='up', to_right=False)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

    def test_find_section_given_words_invalid_include(self):
        with self.assertRaises(ValueError):
            self.ctoc.find_section_given_words("REMS", outfmt='simple', include='invalid', to_right=False)

    def test_find_section_given_words_invalid_outfmt(self):
        with self.assertRaises(ValueError):
            self.ctoc.find_section_given_words("REMS", outfmt='invalid', include='up', to_right=False)

if __name__ == "__main__":
    unittest.main()