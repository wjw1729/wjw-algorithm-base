n = int(input())
a = [int(x) for x in input().split()]

b = [0] * (n - 1)

for i in range(n - 1):
    b[i] = abs(a[i] - a[i + 1])

presum = [0] * (n)

for i in range(1, n):
    presum[i] = presum[i - 1] + (-1) ** i * b[i - 1]

ans = 0

odd = float('inf')
even = 0
for i in range(1, n):
    if i % 2 == 0:
        ans = max(ans, presum[i] - odd)
        even = max(presum[i], even)

    else:
        ans = max(ans, -(presum[i] - even))
        odd = min(presum[i], odd)

print(ans)
