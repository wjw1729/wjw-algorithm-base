# 贪心
class Solution:
    def minimalKSum(self, nums, k: int) -> int:

        nums.sort()
        cnt = 0
        less=0
        for i, num in enumerate(nums):
            if num==47:
                1==1
            cnt =  num - less-1
            if i==0 or nums[i]!=nums[i-1]:
                less+=1
            if cnt >= k:
                break

        if cnt > k:
            ans = (1 + num + k - cnt-1) * (num + k - cnt-1) // 2 - sum(nums[:i])
        elif cnt == k:
            ans = (1 + num) * (num) // 2 - sum(nums[:i + 1])
        else:
            ans = (1 + num + k - cnt) * (num + k - cnt) // 2 - sum(nums)

        return ans


nums=[96,44,99,25,61,84,88,18,19,33,60,86,52,19,32,47,35,50,94,17,29,98,22,21,72,100,40,84]
k=35
res=Solution().minimalKSum(nums,k)
print(res)