"""
author:wjw
分析:记每行总长度为n,则最多可能有n-1个断点，记录断电次数于brkp[]中，得到次数最大的数即可

优化：用字典明显更快
"""
import time
class Solution:
    def leastBricks(self, wall) -> int:
        rowsum = sum(wall[0])
        if rowsum == 1:
            return len(wall)
        d={}
        max_num=0
        for i in range(len(wall)):
            row = wall[i]
            brkpoint = 0
            for j in range(len(row)):
                brkpoint += row[j]
                if brkpoint != rowsum:
                    if brkpoint in d.keys():
                        d[brkpoint]+=1
                    else:
                        d[brkpoint]=1
        if d=={}:
            return len(wall)
        return len(wall) - max(d.values())



t1=time.time()
wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
# wall = [[1],[1],[1]]
# wall=[[100000000],[100000000],[100000000]]
res=Solution().leastBricks(wall)
print(res)
print(time.time()-t1)