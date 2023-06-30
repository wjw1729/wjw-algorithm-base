"""
"""


class Solution:
    def Palindrome(self, s):
        news = ''
        for ch in s:
            news += '#'
            news += ch
        news += '#'

        n = len(news)
        d1 = [0] * n

        l = 0
        r = -1

        for i in range(n):
            k = 1 if i > r else min(d1[l + r - i], r - i + 1)

            while i - k >= 0 and i + k < 0 and news[i - k] == news[i + k]:
                k += 1

            d1[i] = k
            k -= 1
            if i + k > r:
                l = i - k
                r = i + k
