class Solution:
    def numberOfSets(self, n: int, k: int) -> int:

        dp = [[0] * (k + 1) for _ in range(n + 1)]



        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(2, n + 1):
            for j in range(1, k + 1):
                if i==j+1:
                    dp[i][j]=1
                    continue
                if j==1:
                    dp[i][j]=i*(i-1)//2
                    continue
                for m in range(2, i - j + 2):
                    dp[i][j] += dp[i + 1 - m][j - 1] * (dp[m][1] - dp[m - 1][1])

        return dp[n][k]

n=30
k=7
res=Solution().numberOfSets(n,k)
print(res%(10**9+7))