nums = [10, 20, 5, 3, 14, 62]


def quick_sort(data, start, end):

    if start >= end:
        return

    pivot = correct_pivot(data, start, end)
    quick_sort(data, start, pivot-1)
    quick_sort(data, pivot+1, end)


def correct_pivot(data, start, end):
    i, j = start, start

    pivot_val = data[end]
    for j in range(start, end):
        if data[j] < pivot_val:
            data[i], data[j] = data[j], data[i]
            i += 1

    data[end], data[i] = data[i], data[end]
    return i


quick_sort(nums, 0, len(nums)-1)
print(nums)