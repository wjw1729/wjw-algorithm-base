
def intersect(l1,r1,l2,r2):
    if r1<l2 or r2<l1:
        return False

    return True


t=int(input())

for _ in range(t):
    l1,r1,l2,r2=[int(x) for x in input().split()]
    if intersect(l1,r1,l2,r2):
        print(max(l1,l2))
    else:
        print(l1+l2)
