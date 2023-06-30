import math
t=int(input())

for _ in range(t):
    m=int(input())
    k=int(math.log(m,10))
    print(m-10**k)
