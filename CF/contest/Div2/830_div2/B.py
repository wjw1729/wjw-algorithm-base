t=int(input())

for _ in range(t):
    n=int(input())
    s=input()
    ans=0
    check=False
    for i in range(n-1,-1,-1):
        if i+1<n and s[i]=='1' and s[i+1]=='0':
            if check:
                ans+=2
            else:
                ans+=1
        if s[i]=='1':
            check=True

    print(ans)