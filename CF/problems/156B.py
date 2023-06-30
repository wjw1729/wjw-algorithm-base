

n,m=[int(x) for x in input().split()]
a=[0]*n
cnt=[0]*(n+1)
for i in range(n):

    a[i]=int(input())
    if a[i]<0:
        cnt[-a[i]]-=1
        m-=1
    else:
        cnt[a[i]]+=1

cm=0
for c in cnt[1:]:
    if c==m:
        cm+=1

for v in a:
    if v>0:
        if cnt[v]!=m:
            print('Lie')
        elif cm==1:
            print('Truth')
        else:
            print('Not defined')
    else:
        if cnt[-v]!=m:
            print('Truth')
        elif cm==1:
            print('Lie')
        else:
            print('Not defined')



