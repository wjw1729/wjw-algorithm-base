"""
author:wjw
分析：用单调栈求最大子序列。
"""
def maxSubnum(nums,k):
    n = len(nums)

    stack=[0]*k
    top=-1
    remain=n-k

    for num in nums:
        while top>=0 and stack[top]<num and remain>0:
            top-=1
            remain-=1

        if top<k-1:
            top+=1
            stack[top]=num
        else:
            remain-=1
    return stack



class Solution:
    def maxNumber(self, nums1, nums2, k: int):

        ans = 0

        l=max(0,k-len(nums2))
        r=min(k,len(nums1))


        for i in range(l,r+1):
            if i==0:
                merge1=[]
            else:
                merge1=maxSubnum(nums1,i)

            if i==k:
                merge2=[]
            else:
                merge2=maxSubnum(nums2,k-i)


            total = 0
            p1 = 0
            p2 = 0
            while True:
                if p1 < i and p2 < k - i:
                    if merge1[p1] < merge2[p2]:
                        total = total * 10 + merge2[p2]
                        p2 += 1
                    elif merge1[p1]==merge2[p2]:
                        tmp1,tmp2=p1+1,p2+1
                        while tmp1<i and tmp2<k-i and merge1[tmp1]==merge2[tmp2]:
                            tmp1+=1
                            tmp2+=1
                        if tmp1==i or (tmp2<k-i and merge1[tmp1]<merge2[tmp2]):
                            total=total*10+merge2[p2]
                            p2+=1
                        else:
                            total=total*10+merge1[p1]
                            p1+=1
                    else:
                        total = total * 10 + merge1[p1]
                        p1 += 1

                if p1 == i:
                    while p2 < k - i:
                        total = total * 10 + merge2[p2]
                        p2 += 1

                if p2 == k - i:
                    while p1 < i:
                        total = total * 10 + merge1[p1]
                        p1 += 1

                if p1 == i and p2 == k - i:
                    break
            ans = max(ans, total)

        res = []
        while ans > 0:
            res.append(ans % 10)
            ans //= 10
        return res[::-1]


nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
nums1=[5,6,8]
nums2=[6,4,0]
k=3
nums1=[3,4,8,9,3,0]
nums2=[6,1,9,1,1,2]
k=6
res=Solution().maxNumber(nums1,nums2,k)
print(res)