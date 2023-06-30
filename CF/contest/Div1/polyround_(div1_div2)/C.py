t = int(input())

for _ in range(t):
    n = int(input())
    s = input()


    f=[0]*(n-1)
    f[0]=1
    for i in range(1,n-1):
        if s[i]==s[i-1]:
            f[i]=f[i-1]+1
        else:
            f[i]=1

    ans=[i+2-f[i] for i in range(n-1)]
    print(*ans)
"""
    def get(n, s):
        cnt = 0
        if s[-1] == '0':
            for i in range(n - 2, -1, -1):
                if s[i] == '0':
                    cnt += 1
                else:
                    break

            return n - (cnt)

        else:
            for i in range(n - 2, -1, -1):
                if s[i] == '1':
                    cnt += 1
                else:
                    break
            return n - (cnt)


    ans = []
    for x in range(2, n + 1):
        ans.append(get(x, s[:x - 1]))
"""

