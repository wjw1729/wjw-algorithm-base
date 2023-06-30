class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:

        n = len(num)

        nums = list(num)
        for _ in range(k):
            check = False
            for i in range(n - 2, -1, -1):
                if nums[i] < nums[i + 1]:
                    for j in range(n - 1, i, -1):
                        if nums[j] > nums[i]:
                            nums[i], nums[j] = nums[j], nums[i]

                            nums[i + 1:] = nums[i + 1:][::-1]
                            check = True
                            break

                    if check:
                        break

        ans = 0
        for i in range(n):
            target = nums[i]
            index = num.find(target, i)
            ans += index - i
            num = num[:i] + num[index] + num[i:index] + num[index + 1:]

        return ans


num = "6975"
k = 8
res = Solution().getMinSwaps(num, k)
print(res)
