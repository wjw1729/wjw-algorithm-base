from collections import deque
from itertools import product
class Solution:
    def lakeCount(self, field) -> int:
        m=len(field)
        n=len(field[0])
        field=[list(x) for x in field]

        ans=0
        for i in range(m):
            for j in range(n):
                if field[i][j]=='W':
                    ans+=1

                    q=deque()
                    q.append((i,j))
                    field[i][j]='.'

                    while q:
                        x,y=q.pop()

                        for nx,ny in product(range(x-1,x+2,),range(y-1,y+2)):
                            if 0<=nx<m and 0<=ny<n and field[nx][ny]=='W':
                                q.append((nx,ny))
                                field[nx][ny]='.'

        return ans