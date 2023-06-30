t=int(input())
for _ in range(t):
    n=int(input())

    ans=[]


    for i in range((n+1)//2):
        ans.append((3*i+1,3*(n-i-1)+2))

    print(len(ans))
    for x in ans:
        print(*x)



