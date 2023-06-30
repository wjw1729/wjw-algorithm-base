
class Solution:
    def perfectMenu(self, materials, cookbooks, attribute, limit: int) -> int:
        n=len(cookbooks)

        ans=-1
        for mask in range(1<<n):
            check=True
            bf,res=0,0
            cost=[0]*5
            for i in range(n):
                if mask==7:
                    1==1
                if mask & (1<<i):
                    for j in range(5):
                        cost[j]+=cookbooks[i][j]
                        if cost[j]>materials[j]:
                            check=False
                            break
                    bf+=attribute[i][1]
                    res+=attribute[i][0]

                    if check==False:
                        break
            if check and bf>=limit:
                ans=max(ans,res)

        return ans
meterials = [3,2,4,1,2]
cookbooks = [[1,1,0,1,2],[2,1,4,0,0],[3,2,4,1,0]]
attribute = [[3,2],[2,4],[7,6]]
limit = 5
meterials = [10,10,10,10,10]
cookbooks = [[1,1,1,1,1],[3,3,3,3,3],[10,10,10,10,10]]
attribute = [[5,5],[6,6],[10,10]]
limit = 1
res=Solution().perfectMenu(meterials,cookbooks,attribute,limit)
print(res)



