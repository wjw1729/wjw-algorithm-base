class Solution:
    def longestNiceSubarray(self, nums) -> int:
        bit_len = 31

        n = len(nums)
        ans = 1
        for i in range(n):

            tmp = 0
            for j in range(31):
                if i + j >= n:
                    break
                if tmp & nums[i + j]:
                    break
                tmp ^= nums[i + j]
                ans = max(ans, j + 1)

        return ans


nums = [135745088, 609245787, 16, 2048, 2097152]
res = Solution().longestNiceSubarray(nums)
print(res)
