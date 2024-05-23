# Time Complexity: O(a * b)
# Space Complexity: O(1)
def contains_common_item(arr1, arr2):
    for i in range(0, (len(arr1))):
        for j in range (0, len(arr2)):
            if arr1[i] == arr2[j]:
                return True

    return False

# Time Complexity: O(a + b)
# Space Complexity: O(a)
def contains_common_item_using_set(arr1, arr2):
    s = set()

    for i in range(0, len(arr1)):
        s.add(arr1[i])

    for i in range(0, len(arr2)):
        if arr2[i] in s:
            return True

    return False

print(contains_common_item_using_set(['a', 'b', 'c', 'x'], ['z', 'y', 'x']))