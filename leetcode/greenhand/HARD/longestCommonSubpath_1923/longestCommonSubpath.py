"""
author:wjw
分析：
"""

class Solution:
    def longestCommonSubpath(self,n,paths):

        def findLength(nums1,nums2):
            def check(length):
                base,mod=113,10**9+9

                hash1=0
                for i in range(length):
                    hash1=(hash1*base+nums1[i])%mod

                bucket={hash1}
                head=pow(base,length-1,mod)
                for i in range(length,len(nums1)):
                    hash1=((hash1-nums1[i-length]*head)*base+nums1[i])%mod
                    bucket.add(hash1)

                hash2=0
                for i in range(length):
                    hash2=(hash2*base+nums2[i])%mod
                if hash2 in bucket:
                    return True
                for i in range(length,len(nums2)):
                    hash2=((hash2-nums2[i-length]*head)*base+nums2[i])%mod
                    if hash2 in bucket:
                        return True
                return False
            left,right=0,min(len(nums1),len(nums2))
            ans=0
            while left<=right:
                mid=(left+right)//2
                if check(mid):
                    ans=mid
                    left=mid+1
                else:
                    right=mid-1

            return  ans

        res=float('inf')
        paths.sort(key=lambda x:len(x))
        n=len(paths)
        for i in range(n):
            for j in range(i+1,n):
                res=min(res,findLength(paths[i],paths[j]))

        return res
n = 5
paths = [[0,1,2,3,4],[2,3,4],[4,0,1,2,3]]
n = 3
paths = [[0],[1],[2]]
n = 5
paths = [[0,1,2,3,4],
                     [4,3,2,1,0]]
res=Solution().longestCommonSubpath(n,paths)
print(res)



