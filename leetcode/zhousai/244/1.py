
def rotate(mat):
    n=len(mat)
    mat1=[[0 for i in range(n)]for i in range(n)]
    for i in range(n):
        for j in range(n):
            mat1[j][i]=mat[i][j]

    return list(reversed(mat1))
class Solution:
    def findRotation(self, mat, target) -> bool:

        for i in range(4):

            if mat == target:
                return True
            mat=rotate(mat)
            print(mat)
        return False




mat = [[0,1],[1,0]]
target = [[1,0],[0,1]]
mat = [[0,0],[1,0]]

target = [[1,0],[0,0]]
res=Solution().findRotation(mat,target)
print(res)