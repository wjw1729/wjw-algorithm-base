"""
author:wjw
分析:写一个判断相邻的函数。
"""


def judge(row, existed_island):
    for eachpoint in row:
        for k in range(len(existed_island)):
            if (eachpoint[0] - 1, eachpoint[1]) in existed_island[k]:
                return k
    return -1


class Solution:
    def numIslands(self, grid):
        m = len(grid)
        n = len(grid[0])

        if max(max(grid)) == '0':
            return 0
        islands = []
        check=False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    if j == 0 or grid[i][j - 1] == '0':
                        astring = [(i, j)]
                        check=True
                    else:
                        astring.append((i, j))

                if grid[i][j] == '0' or j == n - 1:
                    if check==True:
                        k = judge(astring, islands)
                        if k != -1:
                            islands[k] = islands[k] + astring
                        else:
                            if astring not in islands:
                                islands.append(astring)

        return len(islands)


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
'''
grid = [["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
        ]
        '''
# grid = [["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]
grid = [['0']]
grid=[["0","0","0","0","0","0","1"]]
res = Solution().numIslands(grid)
print(res)
