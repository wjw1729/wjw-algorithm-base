s = input()


def solve():
    n = s.count('#')
    ans = []

    res = s.count('(') - s.count(')')
    if res < n:
        print(-1)
        return

    cnt = 0

    i = 0
    for c in s:
        if c == '(':
            cnt += 1
        elif c == ')':
            cnt -= 1
        else:
            if cnt <= 0:
                print(-1)
                return
            i += 1
            if i < n:
                ans.append(1)
                res -= 1
                cnt -= 1
            else:
                ans.append(res)
                cnt -= res

        if res < 0 or cnt < 0:
            print(-1)
            return

    for c in ans:
        print(c)

    return


solve()
