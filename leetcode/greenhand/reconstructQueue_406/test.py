class Solution:
    def findBestValue(self, arr, target: int) -> int:
        def minabs(arr, pivot):
            sums = sum(x if x < pivot else pivot for x in arr)
            return sums

        left = 0
        right = max(arr)
        ans = right
        cmpv = float('inf')
        while left <= right:
            mid = (left + right) // 2
            tmp = minabs(arr, mid)
            if tmp < target:
                if target - tmp < cmpv:
                    ans = mid
                    cmpv = target - tmp
                if target - tmp == cmpv:
                    ans = min(ans, mid)
                left = mid + 1
            else:
                if tmp - target < cmpv:
                    ans = mid
                    cmpv = tmp - target
                if tmp - target == cmpv:
                    ans = min(ans, mid)
                right = mid - 1

        return ans


arr = [48772, 52931, 14253, 32289, 75263]
target = 40876
res = Solution().findBestValue(arr, target)
print(res)
