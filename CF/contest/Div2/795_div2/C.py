
def sumofsubs(s,k):

    first=None
    end=None
    ans=0
    for i in range(n):
        if first==None and s[i]=='1':
            first=i
            if i==0:
                ans+=10
            elif i==n-1:
                ans+=1
            else:
                ans+=11
        elif s[i]=='1':
            end=i
            if i==0:
                ans+=10
            elif i==n-1:
                ans+=1
            else:
                ans+=11

    if first!=None and end==None:
        if  n-1-first<=k:
            ans=1

        elif  first<=k:
            ans=10




    else:
        if end!=None and end!=n-1 and n-end-1<=k:
            ans-=10
            k-=n-end-1
        if first!=None and first!=0 and first<=k:
            ans-=1
            k-=first

    return ans




t=int(input())

for _ in range(t):
    n,k=[int(x) for x in input().split()]
    s=input()
    res=sumofsubs(s,k)
    print(res)
