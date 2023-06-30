t = int(input())

for _ in range(t):
    n, m = [int(x) for x in input().split()]
    a = input()
    b = input()


    def solve():
        if a[n - m + 1:] != b[1:]:
            return False

        return b[0] in a[:n - m+1]


    if solve():
        print('YES')
    else:
        print('NO')
