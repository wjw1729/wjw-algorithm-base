"""
author:wjw
分析:记每行总长度为n,则最多可能有n-1个断点，记录断电次数于brkp[]中，得到次数最大的数即可
"""
import time
class Solution:
    def leastBricks(self, wall) -> int:
        rowsum = sum(wall[1])
        if rowsum == 1:
            return len(wall)
        brkp = [0] * (rowsum - 1)
        max_num=0
        for i in range(len(wall)):
            row = wall[i]
            brkpoint = 0
            for j in range(len(row)):
                brkpoint += row[j]
                if brkpoint != rowsum:
                    brkp[brkpoint - 1] += 1
                    max_num=max(max_num,brkp[brkpoint - 1])

        return len(wall) - max_num



t1=time.time()
wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
wall = [[1],[1],[1]]
wall=[[100000000],[100000000],[100000000]]
res=Solution().leastBricks(wall)
print(res)
print(time.time()-t1)