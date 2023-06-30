"""
author:wjw
分析：回溯算法。

"""


class Solution:
    def splitIntoFibonacci(self, s):

        n = len(s)
        ans = []

        def backtrack(index):
            if index == n:
                return len(ans) >= 3

            curr = 0
            for i in range(index, n):
                if i > index and s[index] == '0':
                    break
                curr = curr * 10 + ord(s[i]) - ord('0')
                if curr > 2 ** 31 - 1:
                    break

                if len(ans) < 2 or curr == ans[-2] + ans[-1]:
                    ans.append(curr)
                    if backtrack(i + 1):
                        return True
                    ans.pop()
                elif len(ans) >= 2 and curr > ans[-2] + ans[-1]:
                    break
            return False

        backtrack(0)
        return ans


s = "123456579"
res = Solution().splitIntoFibonacci(s)
print(res)
