"""
author:wjw
分析：哈希（Robin Karp算法）+二分查找
    时间复杂度:O((N+M)*log(min(N,M)))
"""


class Solution:
    def findLength(self, nums1, nums2):
        base, mod = 113, 10 ** 9 + 9

        def check(length):
            hash1 = 0
            for i in range(length):
                hash1 = (hash1 * base + nums1[i]) % mod
            bucket1 = {hash1}
            head = pow(base, length - 1, mod)
            for i in range(length, len(nums1)):
                hash1 = ((hash1 - nums1[i - length] * head) * base + nums1[i]) % mod
                bucket1.add(hash1)

            hash2 = 0
            for i in range(length):
                hash2 = (hash2 * base + nums2[i]) % mod
            if hash2 in bucket1:
                return True
            for i in range(length, len(nums2)):
                hash2 = ((hash2 - nums2[i - length] * head) * base + nums2[i]) % mod
                if hash2 in bucket1:
                    return True

            return False

        left, right = 0, min(len(nums1), len(nums2))
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans


nums1 = [1, 2, 3, 2, 1]
nums2 = [3, 2, 1, 4, 7]
nums2=[3,2,1,4]
res = Solution().findLength(nums1, nums2)
print(res)
