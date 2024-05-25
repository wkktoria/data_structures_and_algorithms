import sys

import unittest


# Time Complexity: O(n)
# Space Complexity: O(1)
def max_sub_array(nums):
    max_sum = -sys.maxsize - 1
    current_max = 0

    for i in range(0, len(nums)):
        current_max += nums[i]

        if current_max > max_sum:
            max_sum = current_max

        if current_max < 0:
            current_max = 0

    return max_sum


class TestMaxSubArray(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_example2(self):
        self.assertEqual(max_sub_array([1]), 1)

    def test_example3(self):
        self.assertEqual(max_sub_array([5, 4, -1, 7, 8]), 23)


if __name__ == "__main__":
    unittest.main()
