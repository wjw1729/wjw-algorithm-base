n1, n2, n3 = [int(x) for x in input().split()]
a1 = [int(x) for x in input().split()]
a2 = [int(x) for x in input().split()]
a3 = [int(x) for x in input().split()]

t1 = sum(a1)
t2 = sum(a2)
t3 = sum(a3)

t = t1 + t2 + t3
ans = max(t - 2 * x for x in [t1, t2, t3])

min1 = [min(x) for x in [a1, a2, a3]]

ans = max(ans, t - 2 * (sum(min1) - max(min1)))

print(ans)
