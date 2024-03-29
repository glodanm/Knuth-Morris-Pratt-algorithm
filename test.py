import unittest

from kmp import kmp_search


class TestKMP(unittest.TestCase):

    def test_positive_result(self):
        string = "abcabcdefabcadabefg"
        pattern = "abca"
        expected = ['[0-3]', '[9-12]']

        self.assertEqual(kmp_search(pattern, string), expected)

    def test_wrong_result(self):
        string = "77777"
        pattern = "7"
        expected = ['[0-1]']

        self.assertNotEqual(kmp_search(pattern, string), expected)


if __name__ == '__main__':
    unittest.main()