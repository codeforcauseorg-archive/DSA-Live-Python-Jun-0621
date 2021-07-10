import random

li = [32, 12, 11, 32, 35]

# for i in range(5):
#     li.append(random.randint(10, 50))


def linear_search(nums, target):

    for i in range(len(nums)):
        if nums[i] == target:
            return i

    return None


print(linear_search(li, 33))
