import unittest

def is_unique(string):
    """
    A function to test whether a string has all unique charaters.
    """
    char_dict={}
    for char in string:
        if char in char_dict:
            return False
        char_dict[char]=True
    
    return True


class Test(unittest.TestCase):
    positive = ["abcd", "fght3", ""]
    negative = ["23d32", "HBR FHJ", "  "]

    def test_is_unique(self):
        for test_pos in self.positive:
            actual = is_unique(test_pos)
            self.assertTrue(actual)

        for test_neg in self.negative:
            actual = is_unique(test_neg)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()