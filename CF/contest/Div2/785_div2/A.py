


t=int(input())

for _ in range(t):
    s=input()

    n=len(s)
    total=sum(ord(x)-ord('a')+1 for x in s)
    alice=max(sum(ord(x)-ord('a')+1 for x in s[0:n//2*2]),sum(ord(x)-ord('a')+1 for x in s[1:n]))

    bob=total-alice
    if alice>bob:
        print('Alice %d'%(alice-bob))
    else:
        print('Bob %d'%(bob-alice))