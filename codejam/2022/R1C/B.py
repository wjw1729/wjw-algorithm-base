
def squary(nums):

    t = sum(nums)
    if N==1 and t==0:
        return 1

    if t==0:
        return False
    total=0
    for i in range(N):
        for j in range(i+1,N):
            total+=nums[i]*nums[j]


    if total%t==0:
        return -total//t

    else:
        return False







t=int(input())



for i in range(t):
    N,K=[int(x) for x in input().split()]
    nums=[int(x) for x in input().split()]
    res=squary(nums)
    if res==False:
        print('Case #%d: %s' % (i + 1, 'IMPOSSIBLE'))
    else:
        print('Case #%d: %d' % (i + 1, res))
