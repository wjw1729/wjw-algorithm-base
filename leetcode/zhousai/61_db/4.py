class Solution:
    def minOperations(self, nums) -> int:

        n = len(nums)

        nums.sort()

        pre = 0

        for i in range(n):
            if nums[i] == pre:
                tmp += 1
                nums[i] += 0.0001 * tmp
            else:
                pre = nums[i]
                tmp = 0

        def can(l, r):
            change = n - (r - l + 1)
            if nums[r] - nums[l] - change - (r - l) <= 0:
                return True
            else:
                return False

        maxl = 0
        maxr = 0
        maxlength = 0
        l = 0
        r = 0
        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                r += 1
            else:
                if r - l > maxr - maxl:
                    maxr = r
                    maxl = l
                l = r = i

        l = maxr
        r = n - 1
        ans = 0
        while l <= r:
            mid = (l + r + 1) // 2
            if can(maxl, mid):
                ans = max(ans, mid - maxl + 1)
                l = mid + 1
            else:
                r = mid - 1

        l = 0
        r = maxl
        while l <= r:
            mid = (l + r + 1) // 2
            if can(mid, maxr):
                ans = max(ans, maxr - mid + 1)
                r = mid - 1
            else:
                l = mid + 1
        return n - ans


nums = [8, 5, 9, 9, 8, 4]
res = Solution().minOperations(nums)
print(res)
