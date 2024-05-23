def two_sum(nums, target):
    d = {} # value: index

    for i in range(0, len(nums)):
        d.update({nums[i]: i})

    for i in range(0, len(nums)):
        complement = target - nums[i]
        if complement in d and d[complement] != i:
            return [i, d[complement]]

    return []

print(two_sum([2,7,11,15], 9))
print(two_sum([3,2,4], 6))
print(two_sum([3,3], 6))