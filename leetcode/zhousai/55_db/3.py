class Solution:
    def maxAlternatingSum(self, nums) -> int:

        n = len(nums)
        for i in range(n-1,0,-1):
            if nums[i]==nums[i-1]:
                nums.pop(i)

        n=len(nums)
        ans = []

        if n==1:
            return nums[0] ##防止下标越界
        for i in range(n):
            if i == 0 and nums[i] > nums[i + 1]:
                ans.append(nums[i])

            if n - 1 > i > 0 and nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                ans.append(nums[i])

            if n - 1 > i > 0 and nums[i] < nums[i - 1] and nums[i] <= nums[i + 1]:
                ans.append(nums[i])

            if i == n - 1 and nums[i] > nums[i - 1]:
                ans.append(nums[i])

        sum_ans = sum(ans) - 2 * sum([ans[i] for i in range(len(ans)) if i % 2 == 1])
        return sum_ans


nums = [4, 2, 5, 3]
nums = [5, 6, 7, 8]
nums = [6, 2, 1, 2, 4, 5]
nums = [6, 2, 4, 4, 4, 3, 2, 2, 7, 9, 8]
#nums = [2, 1, 5, 4, 4]
#nums=[4,3,13,4,12,12,20,9,2,15]
res = Solution().maxAlternatingSum(nums)
print(res)
