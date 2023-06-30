class Solution:
    def brilliantSurprise(self, present, limit) -> int:

        dp=[0]*(limit+1)
        ans=0


        def f(a,total):
            nonlocal  dp,ans

            if len(a)==1:
                s=0
                for i,x in enumerate(a[0]):
                    if i>=limit:
                        break
                    s+=x
                    ans=max(ans,dp[limit-(i+1)]+s)
                return

            tmp=dp.copy()
            m=len(a)//2
            left,right=a[:m],a[m:]

            #计算左侧01背包
            for i,row in enumerate(left):
                for j in range(limit,len(row)-1,-1):
                    dp[j]=max(dp[j],dp[j-len(row)]+total[i])

            f(right,total[m:])

            dp=tmp

            for i,row in enumerate(right):
                for j in range(limit,len(row)-1,-1):
                    dp[j]=max(dp[j],dp[j-len(row)]+total[m+i])

            f(left,total[:m])


            #


        total=[sum(a) for a in present]
        f(present,total)

        return ans

present=[[5,8],[3,6,8],[4,5],[2,4],[2,5],[7],[2,7],[3],[4,8]]
limit=4
present=[[5,10],[1,2,3],[1,20]]
limit=3
res=Solution().brilliantSurprise(present,limit)
print(res)