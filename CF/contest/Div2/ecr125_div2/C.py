
t=int(input())

for _ in range(t):
    n=int(input())
    s=input()

    ans=0
    res=n
    l=0

    while l<n:

        if s[l]=='(':
            if l+2>n:
                break
            l+=2
            ans+=1
            res-=2
        else:
            r=l+1
            while r<n and s[r]!=')':
                r+=1
            if r>=n:
                break
            ans+=1
            res-=r-l+1
            l=r+1

    print(ans,res)



