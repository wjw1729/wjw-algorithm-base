"""
author:wjw
分析：
"""


class Solution:
    def compareVersion(self, version1, version2):
        version1 = version1.split('.')
        version2 = version2.split('.')

        length = max(len(version1), len(version2))

        for i in range(length):
            nums1 = int(version1[i]) if i < len(version1) else 0
            nums2 = int(version2[i]) if i < len(version2) else 0

            if nums1 > nums2:
                return 1
            if nums1 < nums2:
                return -1

        return 0


version1='1.01'
version2='1.0001'
res=Solution().compareVersion(version1,version2)
print(res)