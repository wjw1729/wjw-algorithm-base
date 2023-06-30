
t=int(input())
for _ in range(t):
    n=int(input())
    a=[int(x) for  x in input().split()]

    print(max(range(n),key=lambda x:a[x])+1)