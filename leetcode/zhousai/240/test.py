

def minDistance(word1,word2):
    m=len(word1)
    n=len(word2)

    dp=[[0]*n for _ in range(m)]

    for i in range(m):
        for j in range(n):

            if word1[i]==word2[j]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=min(dp[i-1][j-1]+1,dp[i-1][j]+1,dp[i][j-1]+1)

    return dp[m-1][n-1]
word1 = "horse"
word2 = "ros"
res=minDistance(word1,word2)
print(res)


