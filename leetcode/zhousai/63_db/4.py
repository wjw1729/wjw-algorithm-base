"""
对于一个正数数组。返回比nums[i]*nums[j]小的数的个数。
"""

import bisect

def smallernums(nums1,nums2,x):
    m=len(nums1)
    n=len(nums2)
    ans=0
    for i in range(m):
        ans+=bisect.bisect(nums2,x//nums1[i])

    return ans



