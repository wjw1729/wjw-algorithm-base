"""
author:wjw
分析:1.前缀和S表示,S[R]-S[L]<=某个数,便利base，直到知道到符合D的最小base（最低载货量）。枚举base，算法复杂度高O(n3)?
    优化方案2.base可以使用二分查找。
"""


class Solution:
    def shipWithinDays(self, weights, D):
        sum = 0
        S = [0]
        for i in range(len(weights)):
            sum = sum + weights[i]
            S.append(sum)

        base = max(S[-1] // D,max(weights))

        for base in range(base,S[-1]):
            left = 0
            num = 0
            right = 0
            while right < len(S)-1:
                for right in range(left, len(S)):
                    if S[right]==55:
                        print('is checked')
                    if S[right] - S[left] > base:
                        num += 1
                        print(left,right)
                        left = right - 1
                        break


            if num <= D-1:
                return base




weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
D = 5
weights=[3,2,2,4,1,4]
D=3
# weights=[1,2,3,1,1]
# D=4
result = Solution().shipWithinDays(weights, D)
print(result)