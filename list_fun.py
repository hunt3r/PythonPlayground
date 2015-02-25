def intersection_slow(arr1, arr2, sort=False):
    intersect_arr = []
    for i in arr1:
        if i in arr2 and i not in intersect_arr:
            intersect_arr.append(i)
    if sort:
        intersect_arr.sort()
    return intersect_arr

print intersection_slow([2, 3, 2 ,2 ,2, 1], [2, 4, 5, 6, 1])

print intersection_slow([2, 3, 2 ,2 ,2, 1], [2, 4, 5, 6, 1], sort=True)
