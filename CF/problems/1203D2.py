s = input()
t = input()

n = len(s)
m = len(t)

idx = [[0, 0] for _ in range(m)]

j = 0
ans = 0

for i in range(n):
    if s[i] == t[j]:
        idx[j][0] = i
        j += 1
    if j==m:
        break

j = m - 1
for i in range(n - 1, -1, -1):
    if s[i] == t[j]:
        idx[j][1] = i
        j -= 1

    if j==-1:
        break

ans = max(ans, idx[0][1])
for i in range(1, m):
    ans = max(ans, idx[i][1] - idx[i - 1][0] - 1)

ans = max(ans, n-1 - idx[m - 1][0])
print(ans)
