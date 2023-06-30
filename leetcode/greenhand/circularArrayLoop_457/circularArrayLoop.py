"""
author:wjw
分析：快慢指针+标记为0.
"""


class Solution:
    def circularArrayLoop(self, nums):
        n = len(nums)

        def next(cur):
            return (cur + nums[cur]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            slow, fast = i, next(i)

            while nums[slow] * nums[fast] > 0 and nums[slow] * nums[next(fast)] > 0:

                if slow == fast:
                    if slow == next(slow):
                        break
                    return True
                slow = next(slow)
                fast = next(next(fast))

            add = i
            while nums[add] * nums[next(add)] > 0:
                tmp = add
                add = next(add)
                nums[tmp] = 0
        return False


nums = [2, -1, 1, 2, 2]
nums = [-1, 2]
nums = [-2, 1, -1, -2, -2]
nums = [-1, -2, -3, -4, -5]
nums=[3,1,2]
res = Solution().circularArrayLoop(nums)
print(res)
