class Solution:
    def kSum(self, nums, k: int) -> int:
        s = sum(x for x in nums if x > 0)
        a = [abs(x) for x in nums]
        p = [0]
        a.sort()
        for x in a[:k]:
            q = [x + y for y in p]
            p = p + q
            p.sort()
            p = p[:k]
            print(q)
        return s - p[k - 1]


nums = [2,4,-2]
k = 5
nums = [1,-2,3,4,-10,12]
k = 16
res=Solution().kSum(nums,k)
print(res)
