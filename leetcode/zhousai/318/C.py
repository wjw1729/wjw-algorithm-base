class Solution:
    def totalCost(self, costs, k: int, candidates: int) -> int:
        hp=[]
        n=len(costs)
        if 2*candidates+k<=n:
            costs.sort()
            return sum(costs[:k])

        l=candidates
        r=n-candidates-1

        for i in range(candidates):
            heapq.heappush(hp,(costs[i],i))

        for  i in range(n-candidates,n):
            heapq.heappush(hp, (costs[i], i))

        ans=0
        for i in range(k):
            a,idx=heapq.heappop(hp)
            if idx<r:
                heapq.heappush(hp,(costs[l],l))
                l += 1
            else:
                heapq.heappush(hp,(costs[r],r))
                r-=1
            ans+=a

        return ans


