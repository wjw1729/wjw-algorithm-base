"""
先实现扰乱算法。
"""
import numpy as np

class Solution:
    def Scramble(self,str):
        if len(str)==1:
            return str

        pos=np.random.randint(1,len(str))
        str1=str[:pos]
        str2=str[pos:]
        prob=np.random.random()
        if prob<0.5:
            outstr=self.Scramble(str1)+self.Scramble(str2)
        else:
            outstr=self.Scramble(str2)+self.Scramble(str1)
        return  outstr



str='great'

str='a'
str='ab'
str='abc'
str='abcd'
str='abcdef'

S=Solution()
list=[]
for i in range(1000000):
    out=S.Scramble(str)
    if out not in list:
        list.append(out)
print(list)
print(len(list))
print('caedb' in list)