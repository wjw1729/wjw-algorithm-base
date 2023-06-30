from collections import defaultdict
import bisect


class Solution:
    def numberOfCombinations(self, num: str) -> int:
        MOD = 10 ** 9 + 7
        if num[0] == '0':
            return 0
        n = len(num)
        dp = [defaultdict(int) for _ in range(n + 1)]
        indexls = [[] for _ in range(n + 1)]
        totaldict = [defaultdict(int) for _ in range(n + 1)]

        dp[0][0] = 1
        indexls[0].append(0)
        totaldict[0][0] = 1

        for i in range(1, n + 1):
            total = 0
            for j in range(i - 1, -1, -1):
                if num[j] == '0':
                    continue
                tmpnum = int(num[j:i])
                index = bisect.bisect(indexls[j], tmpnum)

                dp[i][tmpnum] += totaldict[j][indexls[j][index - 1]] if index!=0 else 0
                dp[i][tmpnum] %= MOD
                indexls[i].append(tmpnum)
                total += dp[i][tmpnum]
                totaldict[i][tmpnum] = total
        return total % MOD


num = '9' * 3000

res = Solution().numberOfCombinations(num)
print(res)
