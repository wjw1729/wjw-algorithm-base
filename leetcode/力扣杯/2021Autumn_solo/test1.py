from collections import defaultdict


class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for i in range(n)]
        index = [[[] for _ in range(n)] for _ in range(n)]

        hashmap = defaultdict(list)

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = 1
                    index[i][j] = [{i}]
                    hashmap[1].append({i})
                    continue
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2

                    if i + 1 > j - 1:
                        index[i][j].append({i, j})
                        continue
                    hashmap[2].append({i, j})
                    for a in index[i + 1][j - 1]:
                        index[i][j].append(a | {i, j})
                        hashmap[dp[i][j]].append(a | {i, j})

                else:
                    if dp[i + 1][j] > dp[i][j - 1]:

                        dp[i][j] = dp[i + 1][j]
                        index[i][j] = index[i + 1][j]
                    elif dp[i + 1][j] < dp[i][j - 1]:
                        dp[i][j] = dp[i][j - 1]

                        index[i][j] = index[i][j - 1]
                    else:
                        dp[i][j] = dp[i][j - 1]

                        index[i][j] = index[i + 1][j] + index[i][j - 1]

        for k1, v1 in sorted(hashmap.items(), key=lambda x: x[0], reverse=True):
            for k2, v2 in sorted(hashmap.items(), key=lambda x: x[0], reverse=True):
                for a in v1:
                    for b in v2:
                        if a & b == set():
                            return k1 * k2


s = "wokkow"
res = Solution().maxProduct(s)
print(res)
