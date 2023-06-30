import heapq
class Solution:
    def mostBooked(self, n: int, meetings) :
        heap=[]
        ans=[0]*n

        meetings.sort()
        idle=[]

        for i in range(n):
            heapq.heappush(heap,(0,i))
        for s,e in meetings:
            if s==49 and e==50:
                1==1
            while heap and heap[0][0]<=s:
                t,i=heapq.heappop(heap)
                heapq.heappush(idle,(i,t))

            if idle:
                i,t=heapq.heappop(idle)
                heapq.heappush(heap,(e,i))
                print((e,i))
                ans[i]+=1
            else:
                t,i=heapq.heappop(heap)
                print(t,i)
                if t>s:
                    heapq.heappush(heap,(t+e-s,i))
                    print((e+t-s, i))
                    ans[i]+=1

                else:
                    heapq.heappush(heap, (e, i))
                    print((e, i))
                    ans[i]+=1


        print(ans)
        return max(range(n),key=lambda x:ans[x])



n = 4
meetings = [[48,49],[22,30],[13,31],[31,46],[37,46],[32,36],[25,36],[49,50],[24,34],[6,41]]
res=Solution().mostBooked(n,meetings)
print(res)