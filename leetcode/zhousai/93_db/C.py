import bisect
class Solution:
    def maxJump(self, stones) -> int:

        n=len(stones)


        def isget(x,stones):

            vis=set()
            i=0
            idx=x
            while idx<stones[-1]:
                j=bisect.bisect_right(stones,idx)

                if j-1<=i:
                    return False
                vis.add(j-1)
                i=j-1
                idx=stones[j-1]+x

            i=n-1
            idx=stones[-1]-x

            stones=[stones[i] for i in range(n) if i not in vis]
            while idx>0:
                j=bisect.bisect_left(stones,idx)

                if j>=i:
                    return False
                i=j
                idx=stones[j]-x

            return True

        l=0
        r=10**9+1
        ans=float('inf')

        while l<=r:
            mid=(l+r+1)//2
            if isget(mid,stones):
                ans=mid
                r=mid-1
            else:
                l=mid+1

        isget(4,stones)

        return ans



stones = [0,2,5,6,7]
res=Solution().maxJump(stones)
print(res)




