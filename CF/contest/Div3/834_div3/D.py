import math

t = int(input())
for _ in range(t):
    n, m = [int(x) for x in input().split()]


    def solve(n, m):
        a2 = 0
        a = n
        while a % 2 == 0:
            a2 += 1
            a //= 2

        a5 = 0
        a = n
        while a % 5 == 0:
            a5 += 1
            a //= 5

        if a5 >= a2:
            d = min(2 ** (a5 - a2), 2 ** (math.floor(math.log2(m))))
        else:
            d = min(5 ** (a2 - a5), 5 ** (math.floor(math.log(m, 5))))

        m //= d

        bits = 0
        while m >= 10:
            m //= 10
            bits += 1

        print(n * m * 10 ** bits * d)


    solve(n, m)
