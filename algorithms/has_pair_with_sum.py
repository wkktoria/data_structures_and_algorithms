# Time Complexity: O(n)
# Space Complexity: O(n)
def has_pair_with_sum(arr, sum):
    s = set()

    for i in range(0, len(arr)):
        if arr[i] in s:
            return True
        else:
            s.add(sum - arr[i])

    return False


print(has_pair_with_sum([3, 2, 1, 5], 7))
