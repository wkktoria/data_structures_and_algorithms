def move_zeros(nums):
    j = 0 # index of leftmost 0

    for i in range(0, len(nums)):
        if i != j and nums[j] == 0:
            nums[i], nums[j] = nums[j], nums[i]
        if nums[j] != 0:
            j += 1

a1 = [0,1,0,3,12]
move_zeros(a1)
print(a1)

a2 = [0]
move_zeros(a2)
print(a2)