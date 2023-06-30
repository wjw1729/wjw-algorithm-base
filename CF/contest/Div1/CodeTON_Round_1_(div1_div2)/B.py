

def canget(nums,k):
    numset=set()

    for num in nums:
        if num+k in numset or num-k in numset:
            return True
        numset.add(num)

    return  False

t=int(input())

for _ in range(t):
    _,k=[int(x) for x in input().split()]
    nums=[int(x) for x in input().split()]
    if canget(nums,k):
        print('YES')
    else:
        print('NO')



