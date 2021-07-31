nums = [10, 45, 3]


class Solution:

    def sortArray(self, nums):
        return self.merge_sort(nums, 0, len(nums)-1)

    def merge_sort(self, data, start, end):
        if (end - start) < 30:
            chop = data[start: end+1]
            self.insertion_sort(chop)
            return chop

        mid = (start + end) // 2

        sorted_left = self.merge_sort(data, start, mid)
        sorted_right = self.merge_sort(data, mid+1, end)
        return self.merge(sorted_left, sorted_right)

    def merge(self, first, second):

        result = []
        i, j = 0, 0

        while (i < len(first)) and (j < len(second)):

            if first[i] < second[j]:
                result.append(first[i])
                i += 1
            else:
                result.append(second[j])
                j += 1

        result.extend(first[i:])
        result.extend(second[j:])

        return result

    def insertion_sort(self, data):
        for sorted_till in range(len(data) - 1):
            for pos in range(sorted_till + 1, 0, -1):
                if data[pos] < data[pos - 1]:
                    data[pos], data[pos - 1] = data[pos - 1], data[pos]
                else:
                    break


sorted_li = Solution().sortArray(nums)
print(sorted_li)