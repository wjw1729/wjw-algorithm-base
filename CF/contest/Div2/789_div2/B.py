def minopofgoodstr(s):
    ans=0
    l=0
    while l<n:
        r=l+1
        while r<n and s[r]==s[r-1]:
            r+=1
        tmp=r-l
        if tmp%2!=0:
            ans+=1
            l=r+1
        else:
            l=r

    return ans

t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    res=minopofgoodstr(s)
    print(res)