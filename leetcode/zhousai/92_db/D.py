class Solution:
    def countPalindromes(self, s: str) -> int:

        n = len(s)
        pre = [[0] * 10 for _ in range(n)]
        presum = sufsum = [[[0] * 10 for _ in range(10)] for _ in range(n)]

        suf = [[0] * 10 for _ in range(n)]

        sufsum = [[[0] * 10 for _ in range(10)] for _ in range(n)]

        cnt = [0] * 10

        for i in range(n):
            if i + 1 < n:
                for c1 in range(10):
                    for c2 in range(10):
                        presum[i][c1][c2] = presum[i - 1][c1][c2]
            for c in range(10):
                pre[i][c] += cnt[c]
                presum[i][int(s[i])][c] += pre[i][c]

            cnt[int(s[i])] += 1

        cnt = [0] * 10
        for i in range(n - 1, -1, -1):
            if i + 1 < n:
                for c1 in range(10):
                    for c2 in range(10):
                        sufsum[i][c1][c2] = sufsum[i + 1][c1][c2]
            for c in range(10):
                suf[i][c] += cnt[c]

                sufsum[i][int(s[i])][c] += suf[i][c]

            cnt[int(s[i])] += 1

        ans = 0
        for i in range(2, n - 2):
            for c1 in range(10):
                for c2 in range(10):
                    ans += presum[i - 1][c1][c2] * sufsum[i + 1][c1][c2]

        return ans


s = "103301"
s = "0000000"
res = Solution().countPalindromes(s)
print(res)
