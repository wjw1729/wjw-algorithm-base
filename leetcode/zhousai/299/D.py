class Solution:
    def minimumScore(self, nums, edges) -> int:


        n=len(nums)
        g=[[] for _ in range(n)]
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)


        time_in,time_out,xor_sum=[0]*n,[0]*n,[0]*n

        c=0
        def dfs(u,parent):
            nonlocal c
            c+=1
            time_in[u]=c
            xor_sum[u]=nums[u]
            for v in g[u]:
                if v==parent:
                    continue
                dfs(v,u)
                xor_sum[u]^=xor_sum[v]

            time_out[u]=c

        dfs(0,-1)


        ans=float('inf')
        for i in range(n-1):
            u1,v1=edges[i]
            if time_in[u1]>time_in[v1]:
                u1,v1=v1,u1
            for j in range(i+1,n-1):
                u2,v2=edges[j]
                if time_in[u2] > time_in[v2]:
                    u2, v2 = v2, u2

                if time_in[v1]<time_in[u2]<=time_out[v1] or v1==u2:
                    sls=[xor_sum[0]^xor_sum[v1],xor_sum[v1]^xor_sum[v2],xor_sum[v2]]
                    ans=min(max(sls)-min(sls),ans)
                elif time_in[v2]<time_in[u1]<=time_out[v2] or v2==u1:
                    sls=[xor_sum[0]^xor_sum[v2],xor_sum[v2]^xor_sum[v1],xor_sum[v1]]
                    ans = min(max(sls) - min(sls), ans)
                else:
                    sls=[xor_sum[v1],xor_sum[v2],xor_sum[0]^xor_sum[v1]^xor_sum[v2]]

                    ans = min(max(sls) - min(sls), ans)


        return ans



nums = [1,5,5,4,11]
edges = [[0,1],[1,2],[1,3],[3,4]]
nums = [5,5,2,4,4,2]
edges = [[0,1],[1,2],[5,2],[4,3],[1,3]]
res=Solution().minimumScore(nums,edges)
print(res)



