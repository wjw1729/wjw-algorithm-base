class Solution:
    def minimumTotalCost(self, nums1, nums2) -> int:

        n=len(nums1)
        cnt=Counter()
        for  x in nums1:
            cnt[x]+=1
        for x in nums2:
            cnt[x]+=1

        if any(v>n for k,v in cnt.items()):
            return  -1

        


