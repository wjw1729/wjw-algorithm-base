"""
author:wjw
分析：经过数学上的分析，我们可以发现首位数字的确定我们可以用k//(n-1)!，该值+1即为首位元素。进一步发散思维我们可以发现，对于排列中的任何一位数我们都可以采用此办法来确定。
    算法流程就是：创建[1,....,n]的数组，目标输出有n位，我们需要进行n-1次迭代，确定前n-1个数，第n个数自动确定。k//(2**k)即可求取该位数的索引。每次取完数后要从数组中pop该数。由于各位的索引是从0开始的
    所以一开始k要-1.
"""

import math


class Solution:
    def getPermutation(self, n, k):
        nums = list(range(1, n + 1))
        ans = ''
        k=k-1
        for i in range(n - 1, 0, -1):
            index = k // math.factorial(i)
            ans += str(nums[index])
            nums.pop(index)
            k = k % (math.factorial(i))
        ans += str(nums[0])

        return ans


n = 4
k = 9
res = Solution().getPermutation(n, k)
print(res)
