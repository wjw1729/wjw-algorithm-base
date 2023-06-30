
from collections import defaultdict

def cantrans(a,b):

    store=defaultdict(int)
    i,j=n-1,n-1

    while i>=0 or j>=0:

        if j>=1 and b[j]==b[j-1]:
            store[b[j]]+=1
            j-=1
        elif i>=0 and j>=0 and b[j]==a[i]:
            i-=1
            j-=1
        else:
            if a[i] not in store:
                return False
            else:
                store[a[i]]-=1
                if store[a[i]]==0:
                    del store[a[i]]
                i-=1

    return True






t=int(input())
for _ in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]
    if cantrans(a,b):
        print('YES')
    else:
        print('NO')

