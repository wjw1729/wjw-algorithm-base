import bisect
class Solution:
    def totalSteps(self, nums):
        ans=0

        n=len(nums)
        pre=None
        indices=[]
        for i in range(n):
            if pre==None or nums[i]>=pre:
                indices.append(i)
                pre=nums[i]

        indices.append(n)
        m=len(indices)
        for i in range(1,m):
            l=indices[i-1]
            r=indices[i]

            tmp=0
            tmpls=nums[l:r]
            check=True
            while check:
                check=False
                for i in range(len(tmpls)-1,0,-1):
                    if tmpls[i]<tmpls[i-1]:
                        tmpls.pop(i)
                        check=True
                tmp+=1




            ans=max(ans,tmp-1)

        return  ans





nums = [4,5,7,7,13]
nums=[7,14,4,14,13,2,6,13]
nums=[10,1,2,3,4,5,6,1,2,3]
nums=[1682,63,124,147,897,1210,1585,1744,1764,1945,323,984,1886,346,481,1059,1388,1483,1516,1842,1868,1877,504,1197,785,955,970,1848,1851,398,907,995,1167,1214,1423,1452,1464,1474,1311,1427,1757,1992,57,1625,1260,700,725]
res=Solution().totalSteps(nums)
print(res)








