class Solution:
    def minOperations(self, nums) -> int:

        maxnum = max(nums)

        for i in range(31):
            if 2 ** i > maxnum:
                break
        mult = i - 1

        n = len(nums)
        addtimes = [0] * n
        for i in range(n):

            while nums[i] % 2 > 0:
                if nums[i] % 2 == 1:
                    addtimes[i] += 1
                nums[i] //= 2

        return mult + sum(addtimes)


nums=[1,5]
res=Solution().minOperations(nums)