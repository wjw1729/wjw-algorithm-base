from collections import defaultdict
import bisect


class Solution:
    def numberOfCombinations(self, num: str) -> int:
        MOD = 10 ** 9 + 7
        if num[0] == '0':
            return 0
        n = len(num)
        dp = [[] for _ in range(n + 1)]
        indexls = [[] for _ in range(n + 1)]

        dp[0].append((0, 1))
        indexls[0].append(0)

        for i in range(1, n + 1):
            for j in range(i - 1, -1, -1):
                if num[j] == '0':
                    continue
                tmpnum = int(num[j:i])
                index = bisect.bisect(indexls[j], tmpnum)
                total = sum(dp[j][x][1] for x in range(index)) % MOD
                dp[i].append((tmpnum, total))
                indexls[i].append(tmpnum)
        return sum(v for k, v in dp[n]) % MOD


num = "327"
num = '9' * 1000
res = Solution().numberOfCombinations(num)
print(res)
