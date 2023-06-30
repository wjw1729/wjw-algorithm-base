
t=int(input())
for _ in range(t):
    n=int(input())
    a=[int(x) for  x in input().split()]
    if a[0]==min(a):
        print('Bob')
    else:
        print('Alice')