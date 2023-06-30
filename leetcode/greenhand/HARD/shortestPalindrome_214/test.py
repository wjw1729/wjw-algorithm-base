class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        base = 131
        MOD = 10 ** 9 + 7

        hashvalue = []
        total = 0

        n = len(s)
        for i in range(n):
            total = (total * base + ord(s[i]) - ord('a') + 1) % MOD
            hashvalue.append(total)

        for i in range(n // 2 + 1):
            if hashvalue[-1] % hashvalue[i] == 0 and n % (i + 1) == 0:
                slen = len(str(hashvalue[i]))
                pattern = '1' + ('0' * (slen - 1) + '1') * (n // (i + 1) - 1)
                if str(hashvalue[-1] // hashvalue[i]) == pattern:
                    return True

        return False

s='abab'
res=Solution().repeatedSubstringPattern(s)
print(res)