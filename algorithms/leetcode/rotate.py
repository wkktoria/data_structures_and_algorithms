import unittest


# Time Complexity: O(n)
# Space Complexity: O(n)
def rotate(nums, k):
    temp = [None] * len(nums)

    for i in range(0, len(nums)):
        temp[(k + i) % len(nums)] = nums[i]

    nums[:] = temp


class TestRotate(unittest.TestCase):
    def test_example1(self):
        # given
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 3
        # when
        rotate(nums, k)
        # then
        self.assertEqual(nums, [5, 6, 7, 1, 2, 3, 4])

    def test_example2(self):
        # given
        nums = [-1, -100, 3, 99]
        k = 2
        # when
        rotate(nums, k)
        # then
        self.assertEqual(nums, [3, 99, -1, -100])


if __name__ == "__main__":
    unittest.main()
