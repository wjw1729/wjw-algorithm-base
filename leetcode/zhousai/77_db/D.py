from collections import deque
import copy
class Solution:
    def maximumMinutes(self, grid) :
        m=len(grid)
        n=len(grid[0])
        def check(t,grid):

            queue=deque()
            vis=set()
            for i in range(m):
                for j in range(n):
                    if grid[i][j]==1:
                        queue.append((i,j,0))
                        vis.add((i,j))
            while queue:
                x,y,nt=queue.popleft()
                if nt>=t:
                    continue
                for nx,ny in[(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                    if 0<=nx<m and 0<=ny<n and grid[nx][ny]==0  and(nx,ny) not in vis:

                        grid[nx][ny]=1
                        queue.append((nx,ny,nt+1))
                        vis.add((nx,ny))

            hqueue=deque()
            pqueue=deque()
            pqueue.append((0,0))
            if grid[0][0]==1:
                return False
            vis=set()
            vis.add((0,0))
            for i in range(m):
                for j in range(n):
                    if grid[i][j]==1:
                        hqueue.append((i,j))

            while pqueue:
                npq = deque()
                while pqueue:
                    x, y = pqueue.popleft()
                    if grid[x][y]==0:
                        for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0 and (nx, ny) not in vis:
                                if (nx, ny) == (m - 1, n - 1):
                                    return True
                                npq.append((nx, ny))
                                vis.add((nx, ny))

                pqueue = npq

                nhq=deque()
                while hqueue:
                    x,y=hqueue.popleft()
                    for nx,ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                        if 0<=nx<m and 0<=ny<n and grid[nx][ny]==0 :
                            grid[nx][ny]=1
                            nhq.append((nx,ny))

                hqueue=nhq


            return False

        l=0
        r=10**9

        ans=-1
        while l<=r:
            mid=(l+r+1)//2
            ng=copy.deepcopy(grid)
            if check(mid,ng):
                l=mid+1
                ans=mid
            else:
                r=mid-1


        return ans

















grid = [[0,2,0,0,0,0,0],[0,0,0,2,2,1,0],[0,2,0,0,1,2,0],[0,0,2,2,2,0,2],[0,0,0,0,0,0,0]]



res=Solution().maximumMinutes(grid)
print(res)



