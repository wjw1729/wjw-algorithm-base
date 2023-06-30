"""
author:wjw
分析：如何获取输入字符串全部可能的扰乱字符串？
"""



class Solution:
    def Scramble(self,str,pos,swap):
        if len(str)==1:
            return str



        str1=str[:pos]
        str2=str[pos:]
        if swap==0:
            outstr=self.Scramble(str1)+self.Scramble(str2)
        if swap==1:
            outstr=self.Scramble(str2)+self.Scramble(str1)
        return  outstr
