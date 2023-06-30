"""
官方答案：此处有一点不好理解，就是存储解码数的数组有（n+1）维，此处理解为将‘’视作为边界条件，情况，即空字符串的解码数也为1，之后的状态转转移方程是在此基础上的，所以省去了很多对于0的判断，都融在了第一个if语句里。所以代码显得很简洁。
自己写的代码部分呢，虽然冗长，但是可能便于理解。所以f[n]表示字符长度为n的字符串的解码数。
"""


class Solution:
    def numDecodings(self, s):
        n = len(s)
        f = [1] + [0] * n
        for i in range(1, n+1):
            if s[i - 1] != '0':
                f[i] += f[i - 1]
            if i > 1 and s[i - 2] != '0' and int(s[i - 2:i]) <= 26:
                f[i] += f[i - 2]
        print(f)
        return f[n]


s = ""
result = Solution().numDecodings(s)
print(result)
