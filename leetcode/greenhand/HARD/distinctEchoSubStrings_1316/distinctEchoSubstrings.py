"""
author:wjw
分析：RB算法
"""


class Solution:
    def distinctEchoSubstrings(self, s):

        base = 131
        MOD = 10 ** 9 + 7

        wordset = set()
        n = len(s)
        presum = [0] * n

        for i in range(n):
            presum[i] = (presum[i - 1] * base + ord(s[i]) - ord('a')) % MOD

        presum = [0] + presum

        def gethash(l, r):
            res = (presum[r + 1] - presum[l] * pow(base, (r - l + 1), MOD)) % MOD
            return res

        for i in range(n):
            for j in range(i, n):
                if 2 * j - i + 1 > n - 1:
                    break
                text1 = gethash(i, j)
                text2 = gethash(j + 1, 2 * j - i + 1)
                if text1 == text2:
                    wordset.add(text1)

        return len(wordset)


s = 'abcabcabc'
res = Solution().distinctEchoSubstrings(s)
print(res)
