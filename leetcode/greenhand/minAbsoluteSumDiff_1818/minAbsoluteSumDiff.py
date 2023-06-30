"""
author:wjw
分析：先求各位对应的绝对值差，再对每个nums2中的值找到其最小的绝对值差优化，则二者之差为ans能狗降低的程度。挑选出最大的abs-diff_change即可。
"""

import bisect


class Solution:
    def minAbsoluteSumDiff(self, nums1, nums2):
        n = len(nums1)
        ans = 0
        maxchange = 0
        diffls = []
        for i in range(n):
            absdiff = abs(nums1[i] - nums2[i])
            ans += absdiff
            diffls.append((absdiff, nums2[i]))

        nums1.sort()

        for i in range(n):
            absdiff, num2 = diffls[i]

            index = bisect.bisect(nums1, num2)
            diff1 = abs(nums1[index - 1] - num2) if index != 0 else float('inf')
            diff2 = abs(nums1[index] - num2) if index != len(nums1) else float('inf')
            diff_change = min(diff1, diff2)
            maxchange = absdiff - diff_change

        return (ans - maxchange) % (10 ** 9 + 7)


nums1 = [1, 7, 5]
nums2 = [2, 3, 5]
nums1 = [1, 10, 4, 4, 2, 7]
nums2 = [9, 3, 5, 1, 7, 4]
# nums1=[5,4,7]
# nums2=[10,8,10]
res = Solution().minAbsoluteSumDiff(nums1, nums2)
print(res)
