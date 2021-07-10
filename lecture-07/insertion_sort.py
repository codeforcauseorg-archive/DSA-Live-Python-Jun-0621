nums = [10, 50, 30, 55, 36, 87, 24]


def insertion_sort(data):
    for sorted_till in range(len(data)-1):
        for pos in range(sorted_till+1, 0, -1):
            if data[pos] < data[pos-1]:
                data[pos], data[pos-1] = data[pos-1], data[pos]
            else:
                break


insertion_sort(nums)
print(nums)

