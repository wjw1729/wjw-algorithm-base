class Solution:
    def countTexts(self, pressedKeys: str) -> int:

        def dp(n, k):
            f = [0] * (n + 1)
            f[0] = 1

            for i in range(1, n + 1):
                for j in range(1, k + 1):
                    if i - j >= 0:
                        f[i] += f[i - j]

            return f[n]

        mod = 10 ** 9 + 7
        n = len(pressedKeys)
        ans = 1
        a = 1
        for i in range(1,n):
            if pressedKeys[i] == pressedKeys[i - 1]:
                a += 1
            else:
                if pressedKeys[i - 1] in ['7', '9']:
                    ans *= dp(a, 4)
                else:
                    ans *= dp(a, 3)
                ans %= mod
                a = 1
        if pressedKeys[-1] in ['7', '9']:
            ans *= dp(a, 4)
        else:
            ans *= dp(a, 3)
        ans %= mod

        return ans

pressedKeys = "222222222222222222222222222222222222"
res=Solution().countTexts(pressedKeys)
print(res)