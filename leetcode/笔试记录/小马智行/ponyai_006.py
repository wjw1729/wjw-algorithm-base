"""
author:wjw
分析：树状数组.
"""

import heapq


class Solution:
    def maxNums(self, k, nums):
        n = len(nums)

        heap = [(-nums[i], i) for i in range(n)]
        heapq.heapify(heap)

        pos = 0
        ans = []
        bin = set()


        counter=[0]*10
        d=[]
        for num in nums:
            tmp=sum(counter[:num])
            d.append(tmp)
            counter[num]+=1
            t=0
        while True:
            tmp = []
            num, idx = heapq.heappop(heap)
            tmp.append((num, idx))

            while d[idx] > k:
                num, idx = heapq.heappop(heap)
                t+=1
                tmp.append((num, idx))

            if idx <= pos:
                ans.append(-num)
                bin.add(idx)
                pos+=1
                tmp.pop()
            else:
                ans.append(-num)
                bin.add(idx)
                k -= d[idx]
                pos += 1
                tmp.pop()

            for x in tmp:
                heapq.heappush(heap, x)
            if k == 0:
                break

        return ans + [nums[i] for i in range(n) if i not in bin]

"""
T = int(input().strip())

for i in range(T):
    k = int(input().strip())
    n = int(input().strip())
    nums = [int(x) for x in input().strip().split()]
    res = Solution().maxNums(k, nums)
    print(' '.join(str(x) for x in res))
    """

nums=[4,2,1,3,5]
res=Solution().maxNums(5,nums)
print(res)
