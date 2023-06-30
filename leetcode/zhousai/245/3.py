"""
author:wjw
分析：任意一个target[a,b,c]三元组最多由三个三元组合并，最少由一个三元组合并。分别为[a,*,*]和[*,b,*]和[*,*,c]，其中*表示小于对位最大值的任意数。
"""

import bisect


class Solution:
    def mergeTriplets(self, triplets, target) -> bool:

        first_check = False
        second_check = False
        third_check = False

        a, b, c = zip(*triplets)

        list_a = list(enumerate(a))
        list_a.sort(key=lambda x: x[1])

        temp = [x[1] for x in list_a]

        left_index = bisect.bisect_left(temp, target[0])
        right_index = bisect.bisect_right(temp, target[0])

        for i in range(left_index, right_index):
            if triplets[list_a[i][0]][1] <= target[1] and triplets[list_a[i][0]][2] <= target[2]:
                first_check = True
                break

        if not first_check:
            return False

        list_a = list(enumerate(b))
        list_a.sort(key=lambda x: x[1])

        temp = [x[1] for x in list_a]

        left_index = bisect.bisect_left(temp, target[1])
        right_index = bisect.bisect_right(temp, target[1])

        for i in range(left_index, right_index):
            if triplets[list_a[i][0]][0] <= target[0] and triplets[list_a[i][0]][2] <= target[2]:
                second_check = True
                break

        if not second_check:
            return False

        list_a = list(enumerate(c))
        list_a.sort(key=lambda x: x[1])

        temp = [x[1] for x in list_a]

        left_index = bisect.bisect_left(temp, target[2])
        right_index = bisect.bisect_right(temp, target[2])

        for i in range(left_index, right_index):
            if triplets[list_a[i][0]][0] <= target[0] and triplets[list_a[i][0]][1] <= target[1]:
                third_check = True
                break

        if not third_check:
            return False

        return True


triplets = [[2, 5, 3], [1, 8, 4], [1, 7, 5]]
target = [2, 7, 5]
triplets = [[1, 3, 4], [2, 5, 8]]
target = [2, 5, 8]
triplets = [[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]]
target = [5, 5, 5]
triplets = [[3, 4, 5], [4, 5, 6]]
target = [3, 2, 5]
res = Solution().mergeTriplets(triplets, target)
print(res)
