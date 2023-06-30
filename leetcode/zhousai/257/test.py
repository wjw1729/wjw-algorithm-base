class Solution:
    def findMiddleIndex(self, nums) -> int:
        n = len(nums)
        presum = [0]
        total = 0
        for num in nums:
            total += num
            presum.append(total)

        sufsum = [0]
        total = 0
        for num in nums[::-1]:
            total += num
            sufsum.append(total)

        sufsum = sufsum[n-1::-1]

        for i in range(n):
            if presum[i] == sufsum[i]:
                return i
        return -1

nums=[2,3,-1,8,4]
res=Solution().findMiddleIndex(nums)
print(res)