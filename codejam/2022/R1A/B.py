


def partition(a1,a2,b):

    b=b+a2

    nums1=[]

    total=sum(a1)+sum(b)
    t1=0

    for c in b:
        if t1+c<=total//2:
            nums1.append(c)
            t1+=c

    for c in a1[::-1]:
        if t1+c<=total//2:
            nums1.append(c)
            t1+=c

    assert t1==total//2

    return nums1




t=int(input())

for i in range(t):
    n=int(input())

    a1=[2**i for i in range(30)]
    a2=[10**9-i for i in range(n-30)]
    print(*(a1+a2),flush=True)

    b=[int(x) for x in input().split()]

    res=partition(a1,a2,b)
    print(*res,flush=True)






