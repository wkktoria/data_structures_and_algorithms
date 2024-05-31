import unittest


# Time Complexity: O(n)
# Space Complexity: O(n)
def first_recurring_character(arr):
    chars = {}

    for i in range(0, len(arr)):
        key = arr[i]
        chars.setdefault(key, 0)
        chars[key] += 1

        if chars[key] >= 2:
            return key

    return None


class TestFirstRecurringCharacter(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(first_recurring_character([2, 5, 1, 2, 3, 5, 1, 2, 4]), 2)

    def test_example2(self):
        self.assertEqual(first_recurring_character([2, 1, 1, 2, 3, 5, 1, 2, 4]), 1)

    def test_example3(self):
        self.assertEqual(first_recurring_character([2, 3, 4, 5]), None)


if __name__ == "__main__":
    unittest.main()
