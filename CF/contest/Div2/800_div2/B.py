

t=int(input())
for _ in range(t):
    n=int(input())
    s=input()

    ans=n

    for i in range(n):
        if i>0 and s[i-1]!=s[i]:
            ans+=i

    print(ans)