from collections import defaultdict

t=int(input())

for _ in range(t):
    n=int(input())
    s=input()

    check=False
    idx={}

    for i in range(n-1):
        if s[i:i+2] in idx :
            if idx[s[i:i+2]]<=i-2:
                check=True
                break


        else:
            idx[s[i:i+2]]=i

    if check:
        print('YES')
    else:
        print('NO')


