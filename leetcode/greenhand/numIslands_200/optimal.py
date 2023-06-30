"""
author:wjw
分析：island 里面只保存岛外围轮廓
"""


def judge(x, y, existed_island):
    for edge in existed_island:
        if x == edge[0] + 1 and y == edge[1]:
            return True
        if x == edge[0] and y == edge[1] + 1:
            return True
    return False


class Solution:
    def numIslands(self, grid):
        island = []
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    check = False
                    for k in range(len(island)):
                        if judge(i, j, island[k]) == True:
                            island[k].append([i, j])
                            check = True
                            break

                    if check == False:
                        island.append([[i, j]])

        return len(island)
