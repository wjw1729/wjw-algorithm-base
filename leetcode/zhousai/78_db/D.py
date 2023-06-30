class Solution:
    def largestVariance(self, s: str) -> int:

        n=len(s)
        f1=[0]*(n)
        cnt=[0]*26
        for i in range(n):
            idx=ord(s[i])-ord('a')
            cnt[idx]+=1
            if all(cnt[idx]>cnt[i] for i in range(26) if i!=idx):
                f[i]=
            if all(cnt[idx]<cnt[i] for i in range(26) if i!=idx):

        pre=[1]*n

        for i in range(n):
            while 
