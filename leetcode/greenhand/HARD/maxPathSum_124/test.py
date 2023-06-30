
class Solution:
    def Mysort(self,arr):
        if not arr:
            return []
        pivot=arr[0]
        left=[x for x in arr[1:] if x<=pivot]
        right=[x for x in arr[1:] if x>pivot]
        return self.Mysort(left)+[pivot]+self.Mysort(right)

arr=[5,2,3,1,4]
res=Solution().Mysort(arr)
print(res)