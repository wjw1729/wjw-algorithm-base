class Solution:
    def maxDistance(self, nums1, nums2) -> int:
        m = len(nums1)
        n = len(nums2)

        pointer = 0
        ans = 0
        for i in range(m):
            if i > pointer:
                pointer += 1


            while pointer < n - 1 and nums2[pointer + 1] >= nums1[i]:
                pointer += 1

            ans = max(ans, pointer - i)
        return ans

nums1 = [55,30,5,4,2]
nums2 = [100,20,10,10,5]
res=Solution().maxDistance(nums1,nums2)
print(res)