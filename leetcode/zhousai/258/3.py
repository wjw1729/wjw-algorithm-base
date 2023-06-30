"""
author:wjw
分析：状压。
"""


class Solution:
    def maxProduct(self, s):
        n = len(s)

        palindrome = []
        for mask in range(1, 1 << n):
            tmp = []
            for j in range(n):
                if mask & (1 << j):
                    tmp.append(s[j])

            if tmp == tmp[::-1]:
                palindrome.append((mask, len(tmp)))

        palindrome.sort(key=lambda x: -x[1])

        ans = 0
        for mask1, l1 in palindrome:
            for mask2, l2 in palindrome:
                if mask1 & mask2 == 0:
                    ans = max(ans, l1 * l2)

        return ans


s = "leetcodecom"
s = "bb"
s = "accbcaxxcxx"
res = Solution().maxProduct(s)
print(res)
