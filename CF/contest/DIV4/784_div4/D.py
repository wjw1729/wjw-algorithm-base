

def colorfulstamp(s):
    sls=s.split('W')
    for s in sls:
        if s=='':
            continue
        if len(set(s))==1:
            return False


    return True


t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    if colorfulstamp(s):
        print('YES')
    else:
        print('NO')
