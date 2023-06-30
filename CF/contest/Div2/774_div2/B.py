

def solve(a):

    a.sort()
    if n%2==1:
        return sum(a[:n//2+1])<sum(a[n//2+1:])
    else:
        return sum(a[:n // 2 ]) < sum(a[n // 2 + 1:])




t=int(input())
for _ in range(t):
    n=int(input())
    a=[int(x) for  x in input().split()]

    if solve(a):
        print('YES')
    else:
        print('NO')