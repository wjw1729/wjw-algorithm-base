
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    mod=998244353

    ans=1
    pre=1
    for i in range(1,n):
        if s[i]==s[i-1]:
            pre*=2
            pre%=mod
        else:
            pre=1

        ans+=pre
        ans%=mod
    print(ans)



