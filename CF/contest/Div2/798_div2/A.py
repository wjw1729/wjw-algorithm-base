from collections import Counter
t=int(input())

for _ in range(t):
    n,m,k=[int(x) for x in input().split()]
    a=input()
    b=input()


    a=''.join(sorted(list(a)))
    b=''.join(sorted(list(b)))

    i,j=0,0
    ans=''





    if a[i]<b[j]:

        for ii in range(i, n + 1):
            if ii < n and a[ii] > b[j]:
                break
            if ii - i >= k:
                break
        ans += a[i:ii]
        i = ii
        chose =0
    else:
        for jj in range(j,m+1):
            if jj<m and b[jj]>a[i]:
                break
            if jj-j>=k:
                break
        ans+=b[j:jj]
        j=jj
        chose=1

    while i<n and j<m:

        if chose==1:
            if a[i]>b[j]:
                ans+=a[i]
                i+=1
                chose=0

            else:
                for ii in range(i, n+1):
                    if ii<n and a[ii] > b[j]:
                        break
                    if ii-i>=k:
                        break
                ans += a[i:ii]
                i = ii
                chose = 0
        else:
            if b[j]>a[i]:
                ans+=b[j]
                j+=1
                chose=1
            else:
                for jj in range(j, m + 1):
                    if jj < m and b[jj] > a[i]:
                        break
                    if jj - j >=k:
                        break
                ans += b[j:jj]
                j = jj
                chose = 1



    print(ans)


