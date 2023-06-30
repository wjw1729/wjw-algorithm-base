
import time
class Solution:
    def shortestPathLength(self,graph):
        n=len(graph)

        queue=[(i,1<<i,0) for i in range(n)]
        bin={(i,1<<i) for i in range(n)}


        while queue:
            node,mask,length=queue.pop(0)
            if mask==2**n-1:
                return length
            for next in graph[node]:
                tmp_mask=mask | (1<<next)
                if (next,tmp_mask) not in bin:
                    queue.append((next,tmp_mask,length+1))
                    bin.add((next,tmp_mask))


t1=time.time()
graph=[[1,2,3,4,5,6,7,8,9,10,11],[0,2,5,6,8],[0,1,4,5,6,9,10,11],[0,4,5,6,8,9,10,11],[0,2,3,5,6,8,10],[0,1,2,3,4,6,8,9,10,11],[0,1,2,3,4,5,8,10,11],[0,8],[0,1,3,4,5,6,7,9,10,11],[0,2,3,5,8,10],[0,2,3,4,5,6,8,9],[0,2,3,5,6,8]]
res = Solution().shortestPathLength(graph)
print(res)
print(time.time()-t1)