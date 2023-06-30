

class Solution:
    def rotateGrid(self,grid,k):
        m=len(grid)
        n=len(grid[0])
        level=min(m//2,n//2)

        level_l=[]
        for i in range(level):

            temp=grid[0+i][i:n-i]
            for j in range(i+1,m-i-1):
                temp.append(grid[j][n-i-1])

            temp+=list(reversed(grid[m-i-1][i:n-i]))
            for j in range(m-i-2,i,-1):
                temp.append(grid[j][i])

            temp=temp[(k%len(temp)):]+temp[:(k%len(temp))]


            grid[i][i:n-i]=temp[:n-2*i]
            for j in range(i+1,m-i-1):
                grid[j][n-i-1]=temp[n-3*i+j-1]

            grid[m-i-1][i:n-i]=list(reversed(temp[m+n-4*i-2:m+2*n-6*i-2]))

            for j in range(m-i-2,i,-1):
                grid[j][i]=temp[2*m+2*n-7*i-4-j]


        return grid

grid = [[40,10],[30,20]]
k = 1
grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
k = 2
res=Solution().rotateGrid(grid,k)
print(res)
