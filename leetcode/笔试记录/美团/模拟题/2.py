"""
翻转数组.(转置)
列表生成式。简洁实现。
"""


class SoLution:
    def trans(self,matrix):
        m = len(matrix)
        n = len(matrix[0])
        ans = [[matrix[i][j] for i in range(m)] for j in range(n)]

        return ans


nm=input().strip().split()
n,m=[int(x) for x in nm]
matrix=[]

for i in range(n):
    tmp=[int(x) for x in input().strip().split()]
    matrix.append(tmp)

print(SoLution().trans(matrix))

