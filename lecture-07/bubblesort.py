nums = [10, 17, 21, 40, 40, 48, 50]


def bubble_sort(data):
    for chance in range(len(data)):
        for index in range(len(data)-chance-1):
            if data[index] > data[index+1]:
                (data[index], data[index+1]) = (data[index+1], data[index])


def bubble_sort_mod(data):
    for chance in range(len(data)):
        count = 0
        for index in range(len(data)-chance-1):
            if data[index] > data[index+1]:
                count += 1
                (data[index], data[index+1]) = (data[index+1], data[index])

        if count == 0:
            return


bubble_sort_mod(nums)

print(nums)
