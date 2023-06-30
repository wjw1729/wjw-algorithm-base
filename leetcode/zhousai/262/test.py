class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:

        n = len(s)
        mod = modulo
        p = power
        hp = power ** (k - 1)

        pp = [pow(p, i) for i in range(k)]

        hashv = 0
        for i in range(k):
            hashv += (ord(s[i]) - ord('a') + 1) * pp[i]


        if hashv%mod == hashValue:
            return s[:k]

        for i in range(1, n - k + 1):
            hashv -= (ord(s[i - 1]) - ord('a') + 1)
            hashv //= p
            hashv += (ord(s[i + k - 1]) - ord('a') + 1)*hp

            if hashv%mod == hashValue:
                return s[i:i + k]


s = "fbxzaad"
power = 31
modulo = 100
k = 3
hashValue = 32
s = "leetcode"
power = 7
modulo = 20
k = 2
hashValue = 0
res=Solution().subStrHash(s,power,modulo,k,hashValue)
print(res)