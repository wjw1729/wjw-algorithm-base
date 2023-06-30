
class Solution:
    def __init__(self):
        self.lock=[1]*3

    def add(self,num):
        self.lock[num]+=1
        return self.lock[num]


obj=Solution()
print(obj.add(0))