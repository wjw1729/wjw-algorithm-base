

def lowbit(x):
    return x & -x

def getleftmore(nums):
    unqiue_nums=list(set(nums))
    unqiue_nums.sort(reverse=True)
    d={c:i+1 for i,c  in enumerate(unqiue_nums)}

    n=len(unqiue_nums)
    c=[0]*(n+1)

    def insert(x,val):
        while  x<n+1:
            c[x]+=val
            x+=lowbit(x)

    def query(x):
        res=0
        while x>0:
            res+=c[x]
            x-=lowbit(x)

        return res

    res=0
    for num in nums:
        insert(d[num],1)
        res+=query(d[num])-1


    return res



def promisingstring2(s):

    total=0
    sums=[[] for _ in range(3)]
    sums[0].append(0)
    for c in s:
        if c=='+':
            total+=1
        else:
            total-=1

        sums[total%3].append(total)

    ans=0
    for nums in sums:
        ans+=getleftmore(nums)


    return ans

t=int(input())

for _ in range(t):
    _=input()
    s=input()
    print(promisingstring2(s))




