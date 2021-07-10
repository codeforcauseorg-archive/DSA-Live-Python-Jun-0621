nums = [10, 50, 30, 55, 36, 87, 24]


def max_index(data, start, end):
    midx = start
    for index in range(start+1, end+1):
        if data[index] > data[midx]:
            midx = index

    return midx


def selection_sort(data):

    length = len(data)
    for chance in range(length):
        midx = max_index(data, 0, length-chance-1)
        data[midx], data[length-chance-1] = data[length-chance-1], data[midx]


selection_sort(nums)

print(nums)


