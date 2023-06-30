
def kgood(n):
    
    for i in range(2,n):
        if i * (i - 1) // 2 >= n:
            break
        if (n-(i-1)*i//2)%i==0:
            return i


    return -1


t=int(input())
for _ in range(t):
    n=int(input())
    print(kgood(n))





