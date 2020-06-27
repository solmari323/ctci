import unittest
import collections

def permutation(a,b):
    """
    Testing whether two strings are permutations of each other, using a character counter.
    """
    # Use default dict to avoid having tomake the key exists check
    chars=collections.defaultdict(int)

    # Base Case
    if len(a) != len(b):
        return False

    for char in a:
        chars[char] += 1
    for char in b:
        chars[char] -= 1

    # Assume that if both a and be have the same characters (from permutation definition)
    # all of the dict values should be equal to zero
    return all(x==0 for x in chars.values())


def permutation_sort(a,b):
    """
    Testing whether two strings are permutations of each other using sorting.
    """
    return sorted(a) == sorted(b)



class Test(unittest.TestCase):
    def test_permutation(self):
        test_true = [("abcd","bcad"),("23dfg","f23dg"),("123456","123465")]
        test_false = [("abcd","efgh"),("2345","1234"),("!df34","!(234")]

        for test_strings in test_true:
            result = permutation(*test_strings)
            self.assertTrue(result)

        for test_strings in test_false:
            result = permutation(*test_strings)
            self.assertFalse(result)

    def test_permutation_sort(self):
        test_true = [("abcd","bcad"),("23dfg","f23dg"),("123456","123465")]
        test_false = [("abcd","efgh"),("2345","1234"),("!df34","!(234")]

        for test_strings in test_true:
            result = permutation_sort(*test_strings)
            self.assertTrue(result)

        for test_strings in test_false:
            result = permutation_sort(*test_strings)
            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()