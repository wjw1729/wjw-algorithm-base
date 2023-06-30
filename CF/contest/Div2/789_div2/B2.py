

t=int(input())
for _ in range(t):
    n=int(input())
    s=input()

    opnum=0
    ans=0
    pre=None
    for i in range(0,n,2):
        if s[i]!=s[i+1]:
           opnum+=1
        else:
            if s[i:i+2]!=pre:
                ans+=1
                pre=s[i:i+2]

    if ans==0:
        print(opnum,1)
    else:
        print(opnum,ans)