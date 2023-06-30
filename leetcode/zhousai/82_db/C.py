import heapq
from collections import Counter
class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1: int, k2: int) -> int:
        n=len(nums1)
        nls=[-abs(nums2[i]-nums1[i]) for i in range(n)]
        nls=list(Counter(nls).items())

        heapq.heapify(nls)

        k=k1+k2
        while nls and k>0:
            n1,a=heapq.heappop(nls)
            if not nls:
                tmp=(-n1)*a
                if tmp<k:
                    return 0
                else:
                    z=k//a
                    r=k%a
                    ans=sum(x**2*y for x,y in nls)
                    ans+=(n1+z+1)**2*r+(n1+z)**2*(a-r)
                    return ans


            else:
                tmp=(nls[0][0]-n1)*a
                if tmp<k:

                    k-=tmp

                    t,b=heapq.heappop(nls)
                    heapq.heappush(nls,(t,b+a))
                else:
                    z=k//a
                    r=k%a
                    ans=sum(x**2*y for x,y in nls)
                    ans+=(n1+z+1)**2*r+(n1+z)**2*(a-r)
                    return ans

        ans = sum(x ** 2 * y for x, y in nls)
        return ans









nums1 = [1,2,3,4]
nums2 = [2,10,20,19]
k1 = 0
k2 = 0
nums1 = [7,11,4,19,11,5,6,1,8]


nums2 = [4,7,6,16,12,9,10,2,10]
k1 = 3
k2 = 6
res=Solution().minSumSquareDiff(nums1,nums2,k1,k2)
print(res)