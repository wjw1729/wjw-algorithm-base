

t=int(input())
for _ in range(t):
    s=input()
    c=input()

    check=False

    for i in range(len(s)):
        if s[i]==c and i%2==0:
            check=True
            break

    if check:
        print('YES')
    else:
        print('NO')
