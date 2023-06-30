from collections import deque


class Solution:
    def shortestSubarray(self, nums, k: int) -> int:
        presum = [0]
        total = 0

        for num in nums:
            total += num
            presum.append(total)

        n = len(nums)
        ans = n + 1

        queue = deque()
        queue.append(0)
        for i in range(1, n + 1):

            while queue and presum[i] - presum[queue[0]] >= k:
                tmp = queue.popleft()
                ans = min(ans, i - tmp)

            while queue and presum[i] <= presum[queue[-1]]:
                queue.pop()
            queue.append(i)

        return ans if ans != n + 1 else -1


nums = [56, -21, 56, 35, -9]
k = 61
nums=[1]
k=1
res = Solution().shortestSubarray(nums, k)
print(res)
