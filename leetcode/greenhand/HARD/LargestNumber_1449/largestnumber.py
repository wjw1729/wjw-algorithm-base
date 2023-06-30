"""
author；wjw
分析：从中找出符合target的组合，然后选择长度最长的。
"""


class Solution:
    def largestNumber(self, cost, target):
        n = len(cost)
        ans = []

        def backtrack(target, S):
            if target == 0:
                ans.append(S)
                return

            if S:
                m = int(S[-1]) - 1
            else:
                m = 0

            for i in range(m, n):
                if cost[i] <= target:
                    S += str(i + 1)
                    backtrack(target - cost[i], S)

                    S = S[:-1]

        backtrack(target, '')
        if not ans:
            return '0'

        maxlength=0
        for i in ans:
            maxlength=max(maxlength,len(i))

        ans=[x for x in ans if len(x)==maxlength]

        for i in range(len(ans)):
            ans[i]=int(''.join(sorted(ans[i],reverse=True)))


        return str(max(ans))



cost = [4, 3, 2, 5, 6, 7, 2, 5, 5]
target = 9
cost = [7,6,5,5,5,6,8,7,8]
target = 12
cost = [2,4,6,2,4,6,4,4,4]
target = 5
cost=[2,4,2,5,3,2,5,5,4]
target=739
"""
cost = [6,10,15,40,40,40,40,40,40]
target = 47
cost=[1,1,1,1,1,1,1,3,2]
target=10"""
res = Solution().largestNumber(cost, target)
print(res)
