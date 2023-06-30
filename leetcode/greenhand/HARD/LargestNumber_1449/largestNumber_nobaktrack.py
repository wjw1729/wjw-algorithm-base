"""
author:wjw
分析：
"""


class Solution:
    def largestNumber(self, cost, target):

        n = len(cost)
        ans = []

        cost_sort = list(enumerate(cost))
        cost_sort.sort(key=lambda x: (x[1], -x[0]))

        def backtrack(target, S):
            if target == 0:
                ans.append(S)
                return

            for i in range(n):
                if ans:
                    return
                if cost_sort[i][1] <= target:
                    S += str(cost_sort[i][0] + 1)
                    backtrack(target - cost_sort[i][1], S)

                    S = S[:-1]

        backtrack(target, '')
        if not ans:
            return '0'
        ans[0] = ''.join(sorted(ans[0], reverse=True))
        return ans[0]


cost = [4, 3, 2, 5, 6, 7, 2, 5, 5]
target = 9

cost = [7, 6, 5, 5, 5, 6, 8, 7, 8]
target = 12

cost = [2, 4, 6, 2, 4, 6, 4, 4, 4]
target = 5

cost = [2, 4, 2, 5, 3, 2, 5, 5, 4]
target = 739

cost = [6, 10, 15, 40, 40, 40, 40, 40, 40]
target = 47

cost = [1, 1, 1, 1, 1, 1, 1, 3, 2]
target = 10

cost=[5,6,7,3,4,6,7,4,8]
target=29
"""
"""
res = Solution().largestNumber(cost, target)
print(res)
