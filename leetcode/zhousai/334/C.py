from sortedcontainers import SortedList
class Solution:
    def maxNumOfMarkedIndices(self, nums) -> int:
        sl = SortedList(nums)

        sl1=SortedList()
        sl2=SortedList()
        ans = 0
        while len(sl)>=2:
            if 2*sl[0]<=sl[-1]:
                tmp=sl[0]
                sl1.add(sl[0])
                sl.remove(sl[0])
            else:
                if not sl2:
                    break

                tmp=sl2[0]
                if 2*sl2[0]>sl[-1]:
                    break
                sl2.add(sl[0])
                sl.remove(sl[0])
                sl1.add(sl2[0])
                sl2.remove(sl2[0])



            idx = sl.bisect_left(2 * tmp)
            sl2.add(sl[idx])
            sl.remove(sl[idx])


            ans += 2

        return ans

nums = [9,2,5,4]
nums=[7,6,8]
res=Solution().maxNumOfMarkedIndices(nums)
print(res)