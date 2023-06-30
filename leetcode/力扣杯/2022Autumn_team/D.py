from collections import  Counter,defaultdict
class Solution:
    def Leetcode(self, words) -> int:
        n=len(words)
        cnt=defaultdict(int)
        for s in words:
            for c in s:
                cnt[c]+=1


        if any(cnt['h']<1 or cnt['e']<4 or cnt['l']<3 or cnt['o']<2 or cnt['t']<1  or cnt['c']<1 or cnt['d']<1):
            return -1





