def canconv(s):
    if s[-1]!='B':
        return False

    anum=0
    bnum=0
    for c in s:
        if c=='A':
            anum+=1
        else:
            bnum += 1
            if anum<bnum:
                return False


    return True


t=int(input())
for _ in range(t):
    s=input()
    if canconv(s):
        print('YES')
    else:
        print('NO')
