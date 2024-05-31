import unittest


# Time Complexity: O(n)
# Space Complexity: O(n)
def two_sum(nums, target):
    d = {}  # value: index

    for i in range(0, len(nums)):
        d.update({nums[i]: i})

    for i in range(0, len(nums)):
        complement = target - nums[i]
        if complement in d and d[complement] != i:
            return [i, d[complement]]

    return []


class TestTwoSum(unittest.TestCase):
    def test_example1(self):
        # given
        nums = [2, 7, 11, 15]
        target = 9
        # when
        result = two_sum(nums, target)
        # then
        self.assertEqual(result, [0, 1])

    def test_example2(self):
        # given
        nums = [3, 2, 4]
        target = 6
        # when
        result = two_sum(nums, target)
        # then
        self.assertEqual(result, [1, 2])

    def test_example3(self):
        # given
        nums = [3, 3]
        target = 6
        # when
        result = two_sum(nums, target)
        # then
        self.assertEqual(result, [0, 1])


if __name__ == "__main__":
    unittest.main()
