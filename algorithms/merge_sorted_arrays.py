def merge_sorted_arrays(arr1, arr2):
    if arr1 == None or arr2 == None:
        return []

    if len(arr1) == 0:
        return arr2
    
    if len(arr2) == 0:
        return arr1

    merged = [None] * (len(arr1) + len(arr2))
    j = 0 # Index for arr1
    k = 0 # Index for arr2

    for i in range(0, len(merged)):
        if (j != len(arr1) and (k == len(arr2) or arr1[j] < arr2[k])):
            merged[i] = arr1[j]
            j += 1
        else:
            merged[i] = arr2[k]
            k += 1

    return merged

print(merge_sorted_arrays([0,3,4,31], [3,4,6,30]))