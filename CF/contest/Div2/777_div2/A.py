


t=int(input())

for _ in range(t):
    n=int(input())
    if n%3==0:
        print(int('21'*(n//3)))
    elif n%3==2:
        print(int('21'*(n//3)+'2'))

    else:
        print(int('12'*(n//3)+'1'))