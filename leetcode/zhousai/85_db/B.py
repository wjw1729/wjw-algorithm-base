class Solution:
    def shiftingLetters(self, s: str, shifts) -> str:

        n = len(s)
        d = [0] * (n + 1)

        for s, t, di in shifts:
            d[s] += 1 if di == 1 else -1
            d[t + 1] -= 1 if di == 1 else -1

        pre = 0
        for i in range(n):
            d[i] += pre
            pre += d[i]

        print(d)
        ans = [''] * n
        for i in range(n):
            ans[i] = chr((ord(s[i]) - 97 + d[i]) % 26 + 97)

        return ''.join(ans)

s = "abc"
shifts = [[0,1,0],[1,2,1],[0,2,1]]
res=Solution().shiftingLetters(s,shifts)
print(res)