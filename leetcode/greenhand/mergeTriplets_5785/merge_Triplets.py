"""
author:wjw
分析：
"""


class Solution:
    def mergeTriplets(self, triplets, target):

        max_sum = [0, 0, 0]
        for a, b, c in triplets:
            if a <= target[0] and b <= target[1] and c <= target[2]:
                max_sum = [max(a, max_sum[0]), max(b, max_sum[1]), max(c, max_sum[2])]
                if max_sum == target:
                    return True

        return False


triplets = [[2, 5, 3], [1, 8, 4], [1, 7, 5]]
target = [2, 7, 5]
triplets = triplets = [[1, 3, 4], [2, 5, 8]]
target = [2, 5, 8]
triplets = [[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]]
target = [5, 5, 5]
triplets = [[3, 4, 5], [4, 5, 6]]
target = [3, 2, 5]
res = Solution().mergeTriplets(triplets, target)
print(res)
