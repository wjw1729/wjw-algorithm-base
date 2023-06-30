from collections import Counter


def solve():
    cnt = Counter(a)
    if len(cnt) == 1:
        if 0 in cnt:
            check = True
        else:
            check = False
    elif len(cnt) == 2:
        if 0 not in cnt:
            check = False
            return check
        itls = sorted(cnt.items())

        check = True
        for k, v in itls:
            if k != 0 and v != 1:
                check = False
                break


    elif len(cnt) == 3:
        if 0 not in cnt:
            return False
        itls = sorted(cnt.items())
        check = bool(itls[0][0] + itls[2][0] == 0)

        for k, v in itls:
            if k != 0 and v != 1:
                check = False
                break


    else:
        check = False

    return check


t=int(input())
for _ in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]

    n=len(a)
    if n==3 or n== 4:
        check=True
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    if a[i]+a[j]+a[k] in a:
                        pass
                    else:
                        check=False
                if not check:
                    break
            if not check:
                break

        if not check:
            print('NO')
        else:
            print('YES')

    else:


        if not solve():
            print('NO')
        else:
            print('YES')


