class Solution:
    def minMaxGame(self, nums: List[int]) -> int:

        while len(nums) > 1：
        n = len(nums)
        nnums = [0] * (n // 2)

        for i in range(0, n, 2):
            if (i // 2) % 2 == 0:
                nnums[i // 2] = min(nums[i], nums[i + 1])
            else:
                nnums[i // 2] = max(nums[i], nums[i + 1])

        nums = nnums[:]
        print(nums)

    return nums[0]