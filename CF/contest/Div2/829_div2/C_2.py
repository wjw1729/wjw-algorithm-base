t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]


    def solve():
        cnt = a.count(1) + a.count(-1)
        if cnt % 2 == 1:
            print(-1)
            return

        ans = []

        i = 0
        while i < n:

            l = i
            r = i + 1

            cnt = 0
            while r < n and a[r] == 0:
                r += 1
                cnt += 1

            if a[l] == 0:
                ans.append((l, r - 1))
                i = r
                continue

            if cnt % 2 == 1:
                if a[r] == a[l]:
                    ans.append((l,l))
                    ans.append((l+1,r))
                    i = r + 1
                else:
                    ans.append((l, r))
                    i = r + 1
            else:
                if a[r] == a[l]:
                    ans.append((l, r))
                    i = r + 1
                else:
                    ans.append((l, r - 1))
                    ans.append((r, r))
                    i = r + 1

        print(len(ans))
        for x in ans:
            print(x[0] + 1, x[1] + 1)


    solve()
