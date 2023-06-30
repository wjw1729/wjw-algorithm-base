class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        def solve(s):
            n = len(s)
            presum = [0] * (n + 1)
            for i in range(1, n + 1):
                presum[i] = presum[i - 1] + int(s[i - 1])

            d = {}
            for i in range(n):
                if s[i] == '1':
                    cnt = 0
                    for j in range(i, n):
                        cnt += (1 if s[j] == '1' else -1)
                        if cnt == 0:
                            d[i] = j
                        elif cnt < 0:
                            break

            def dfs(i, j):
                if i > j:
                    return ''

                res = s[i:j + 1]
                cnt = 0
                for idx in range(i, j):
                    if s[idx] == '1':
                        cnt += 1
                    else:
                        cnt -= 1
                    if cnt == 0:
                        res = max(res, dfs(idx + 1, j) + dfs(i, idx))

                for ii in range(i + 1, j + 1):
                    if ii in d:
                        jj = d[ii]
                        if jj <= j:
                            res = max(res, s[i:ii] + dfs(ii, jj) + s[jj + 1:j + 1])
                            break

                return res

            return dfs(0, n - 1)

        ans = solve(s)
        while ans != s:
            s = ans
            ans = solve(s)

        return ans


s = "10101101100010"
res = Solution().makeLargestSpecial(s)
print(res)
