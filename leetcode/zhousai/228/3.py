class Solution:
    def minimumSize(self, nums, maxOperations: int) -> int:

        def minloss(nums, x):
            minop = 0
            for num in nums:
                minop += (num - 0.001) // x

            return minop

        l = 1
        r = max(nums)

        print(minloss(nums,492))

        ans = r
        while l <= r:
            mid = (l + r + 1) // 2

            if minloss(nums, mid) > maxOperations:
                l = mid + 1
            else:
                if mid==492:
                    print(1)
                ans = min(ans, mid)
                r = mid - 1

        return ans



nums=[4,412,354,607,587,28,136,327,929,905,671,811,572,152,556,96,205,188,505,14,602,591,802,662,543,781,878,812,539,981,587,716,531,354,92,165,352,522,983,966,378,911,873,606,392,927,426,726,892,939,96,419,769,387,178,895,41,291,437,513,37,569,945,102,460]
maxOperations=33
res=Solution().minimumSize(nums,maxOperations)
print(res)