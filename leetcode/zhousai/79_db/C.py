class Solution:
    def maximumImportance(self, n: int, roads) -> int:
        indeg = [0] * n

        for u,v in roads:
            indeg[u]+=1
            indeg[v]+=1


        indeg.sort()

        ans=0
        for i in range(n):
            ans+=(i+1)*indeg[i]


        return ans
