import unittest


# Time Complexity: O(n)
# Space Complexity: O(1)
def move_zeros(nums):
    j = 0  # index of leftmost 0

    for i in range(0, len(nums)):
        if i != j and nums[j] == 0:
            nums[i], nums[j] = nums[j], nums[i]
        if nums[j] != 0:
            j += 1


class TextMoveZeros(unittest.TestCase):
    def test_example1(self):
        # given
        nums = [0, 1, 0, 3, 12]
        # when
        move_zeros(nums)
        # then
        self.assertEqual(nums, [1, 3, 12, 0, 0])

    def test_example2(self):
        # given
        nums = [0]
        # when
        move_zeros(nums)
        # then
        self.assertEqual(nums, [0])


if __name__ == "__main__":
    unittest.main()
