"""
author:wjw
分析：逆流。递归实现
    时间复杂度：O（m*n）
"""

class Solution:
    def pacificAtlantic(self,heights):
        m,n=len(heights),len(heights[0])
        pac=[[0]*n for _ in range(m)]
        atl=[[0]*n for _ in range(m)]

        ans=[]
        def reverseflow(r,c,flow):
            if flow[r][c]==1:
                return
            flow[r][c]=1
            if pac[r][c]==1 and atl[r][c]==1:
                ans.append([r,c])

            for x,y in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                if 0<=x<m and 0<=y<n and heights[x][y]>=heights[r][c]:
                    reverseflow(x,y,flow)


        for i in range(m):
            reverseflow(i,0,pac)
            reverseflow(i,n-1,atl)

        for j in range(n):
            reverseflow(0,j,pac)
            reverseflow(m-1,j,atl)

        return ans

heights=[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
res=Solution().pacificAtlantic(heights)
print(res)

