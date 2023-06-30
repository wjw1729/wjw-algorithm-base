from collections import Counter


def yange(l1):
    n = len(l1)
    d = Counter(l1)

    for k, v in d.items():
        if v > 1:
            return False

    l2 = sorted(l1)
    if l1 == l2:
        return True
    else:
        return False


class Solution:
    def canBeIncreasing(self, nums) -> bool:
        if yange(nums):
            return True

        n = len(nums)
        for i in range(n):
            nums2 = [0] * n
            nums2[:] = nums
            nums2.pop(i)
            if yange(nums2):
                return True
        return False

num=[1,2,10,5,7]
num=[2,3,1,2]
num = [1,1,1]
num=[1,2,3]
res=Solution().canBeIncreasing(num)
print(res)

