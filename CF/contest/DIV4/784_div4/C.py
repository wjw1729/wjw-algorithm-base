

def EvenIncrements(nums):
    odd=[nums[i]%2 for i in range(n) if i%2==1]
    even=[nums[i]%2 for i in range(n) if i%2==0]

    return len(set(odd))==1 and len(set(even))==1








t=int(input())
for _ in range(t):
    n=int(input())
    nums=[int(x) for x in input().split()]
    if EvenIncrements(nums):
        print('YES')
    else:
        print('NO')