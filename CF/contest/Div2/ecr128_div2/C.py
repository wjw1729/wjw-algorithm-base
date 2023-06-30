"""
有点难理解，不过时间复杂度为O(n)
"""

def mincost(s):
    n=len(s)
    nums1=s.count('1')
    n0=0

    for i in range(nums1):
        if s[i]=='0':
            n0+=1
    res=n0
    for j in range(nums1,n):
        if s[j]=='0':
            n0+=1
        if s[j-nums1]=='0':
            n0-=1

        res=min(res,n0)

    return res






t=int(input())

for _ in range(t):
    s=input()

    res=mincost(s)
    print(res)
