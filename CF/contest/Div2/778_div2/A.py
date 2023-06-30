


t=int(input())
for i in range(t):
    n=int(input())
    nums=[int(x) for x in input().split()]
    maxnum1=0
    maxnum2=0
    for num in nums:
        if num>maxnum1:
            maxnum2=maxnum1
            maxnum1=num
        elif num>maxnum2:
            maxnum2=num

    print(maxnum1+maxnum2)