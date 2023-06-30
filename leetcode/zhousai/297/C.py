class Solution:
    def distributeCookies(self, cookies, k: int) -> int:

        cls=[0]*k
        n=len(cookies)
        ans=float('inf')

        def dfs(i):
            nonlocal  ans
            if i==n:
                ans=min(ans,max(cls))
                return

            if max(cls)>=ans:
                return



            for j in range(k):
                cls[j]+=cookies[i]
                dfs(i+1)

                cls[j]-=cookies[i]


        cookies.sort(reverse=True)
        dfs(0)
        return ans



