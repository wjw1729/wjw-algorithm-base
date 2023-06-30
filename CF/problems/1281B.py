t = int(input())

for _ in range(t):
    s, c = input().split()

    s = list(s)
    n = len(s)
    f = [0] * n
    minidx = n - 1
    for i in range(n - 1, -1, -1):
        if s[i] < s[minidx]:
            minidx = i
            f[i] = minidx
        elif s[i] == s[minidx]:
            f[i] = i
        else:
            f[i] = minidx

    for i in range(n):
        if f[i] != i:
            s[i], s[f[i]] = s[f[i]], s[i]
            break
    res = ''.join(s)

    if res < c:
        print(res)
    else:
        print('---')
