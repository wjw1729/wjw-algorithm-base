"""
author:wjw
分析：时间复杂度：O(m+n)
    空间复杂度：O(1)
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)

        maxnum = 0
        for i in range((m + n) // 2 + 1):
            submaxnum = maxnum

            if not nums2 or (nums1 and nums2 and nums1[0] < nums2[0]):
                maxnum = nums1.pop(0)
            else:
                maxnum = nums2.pop(0)

        return maxnum if (m + n) % 2 == 1 else (maxnum + submaxnum) / 2


nums1 = [1, 3]
nums2 = [2]
res = Solution().findMedianSortedArrays(nums1, nums2)
print(res)
