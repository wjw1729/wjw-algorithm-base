from sortedcontainers import SortedList
import bisect
class Solution:
    def goodTriplets(self, nums1, nums2) -> int:
        ans = 0
        n = len(nums1)

        points = [(i, nums1[i], nums2[i]) for i in range(n)]

        points.sort(key=lambda x: (x[1], x[2]))

        sl = SortedList()

        pre = [0] * n
        for i, x, y in points:
            index = bisect.bisect(sl, y)
            pre[i] = index

            sl.add(y)

        sl = SortedList()
        after = [0] * n
        points.sort(key=lambda x: (-x[1], -x[2]))

        l = 0
        for i, x, y in points:
            index = bisect.bisect(sl, y)
            after[i] = l - index

            sl.add(y)
            l += 1

        for i in range(n):
            ans += pre[i] * after[i]

        print(pre)
        print(after)
        return ans

nums1=[13,14,10,2,12,3,9,11,15,8,4,7,0,6,5,1]
nums2=[8,7,9,5,6,14,15,10,2,11,4,13,3,12,1,0]
res=Solution().goodTriplets(nums1,nums2)
print(res)

