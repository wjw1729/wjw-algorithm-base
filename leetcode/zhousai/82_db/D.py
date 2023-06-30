class Solution:
    def validSubarraySize(self, nums, threshold: int) -> int:
        n = len(nums)

        nls = [(threshold - 1) // x + 1 if threshold % x != 0 else threshold // x + 1 for x in nums]

        def getleftlower(nls):

            stack = []
            l = [0] * n

            for i in range(n):
                while stack and nls[stack[-1]] <= nls[i]:
                    stack.pop()

                if stack:
                    l[i] = i - stack[-1] - 1
                else:
                    l[i] = i

                stack.append(i)

            return l

        l = getleftlower(nls)
        r = getleftlower(nls[::-1])[::-1]

        for i in range(n):
            if l[i] + r[i] + 1 >= nls[i]:
                return l[i] + r[i] + 1

        return -1


nums = [818, 232, 595, 418, 608, 229, 37, 330, 876, 774, 931, 939, 479, 884, 354, 328]
t = 3790
nums = [6, 5, 6, 5, 8]
t = 7
res = Solution().validSubarraySize(nums, t)
print(res)
