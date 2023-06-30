


t=int(input())
for _ in range(t):
    n=int(input())
    nums=[int(x) for x in input().split()]
    if 0 in nums:
        print(len([x for x in nums if x!=0] ))
    elif len(set(nums))==n:
        print(n+1)
    else:
        print(n)