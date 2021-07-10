import random

li = [13, 17, 22, 23, 24, 35, 41, 44, 45, 47]

# for i in range(10):
#     li.append(random.randint(10, 50))

li.sort()
print(li)


def binay_search(nums, target):
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid

        if target < nums[mid]:
            end = mid-1
        else:
            start = mid+1

    return None


