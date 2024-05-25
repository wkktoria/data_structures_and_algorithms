import unittest


# Time Complexity: O(n)
# Space Complexity: O(n)
def contains_duplicate(nums):
    s = set(nums)
    return len(s) != len(nums)


class TestContainsDuplicate(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(contains_duplicate([1, 2, 3, 1]), True)

    def test_example2(self):
        self.assertEqual(contains_duplicate([1, 2, 3, 4]), False)

    def test_example3(self):
        self.assertEqual(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), True)


if __name__ == "__main__":
    unittest.main()
