


t=int(input())
for _ in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]

    odnum=0
    evennum=0
    for c in a:
        if c%2==1:
            odnum+=1
        else:
            evennum+=1





    print(n-max(odnum,evennum))





