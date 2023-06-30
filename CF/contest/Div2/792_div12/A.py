


t=int(input())

for _ in range(t):
    s=input()

    n=len(s)
    if n==2:
        print(int(s[1]))
    else:
        print(min(int(x) for  x in s))

