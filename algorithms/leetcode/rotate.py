def rotate(nums, k):
    temp = [None] * len(nums)

    for i in range(0, len(nums)):
        temp[(k + i) % len(nums)] = nums[i]

    nums[:] = temp

a1 = [1,2,3,4,5,6,7]
k1 = 3
rotate(a1, k1)
print(a1)

a2 = [-1,-100,3,99]
k2 = 2
rotate(a2, k2)
print(a2)