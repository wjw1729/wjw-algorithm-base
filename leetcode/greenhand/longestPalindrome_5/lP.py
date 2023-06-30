"""
author:wjw
分析：如果是回文，则最少会出现bb或者aba的结构，找到这个结构再沿两边扩展搜索

"""


def findthemincell(s):
    if len(s) == 1:
        return []
    l = []
    for i in range(len(s) - 2):
        if s[i] == s[i + 1]:
            l.append([i, i + 1])

        if s[i] == s[i + 2]:
            l.append([i, i + 2])
    if s[len(s) - 2] == s[len(s) - 1]:
        l.append([len(s) - 2, len(s) - 1])
    return l


class Solution:
    def longestPalindrome(self, s):

        l = findthemincell(s)
        if l == []:
            return s[0]

        pal = ''
        for index in l:
            left = index[0]
            right = index[1]
            huiwen = s[left + 1:right]
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                huiwen = s[left] + huiwen + s[right]
                left -= 1
                right += 1

            if len(pal) < len(huiwen):
                pal = huiwen

        return pal


str = 'ac'
result = Solution().longestPalindrome(str)
print(result)
