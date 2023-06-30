class Solution:
    def sellingWood(self, m: int, n: int, prices) -> int:

        f=[[0]*(n+1)  for _ in range(m+1)]

        for h,w,p in prices:
            f[h][w]=max(f[h][w],p)



        for i in range(1,m+1):
            for j in range(1,n+1):

                for jj in range(1,j):
                    f[i][j]=max(f[i][j],f[i][jj]+f[i][j-jj])

                for ii in range(1,i):
                    f[i][j]=max(f[i][j],f[ii][j]+f[i-ii][j])


        return f[m][n]