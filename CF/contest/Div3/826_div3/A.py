
t=int(input())

for _ in range(t):
    a,b=input().split()

    def mycomp(a,b):
        if a[-1]=='L':
            if b[-1]=='L':
                return len(a)>len(b)
            else:
                return True
        elif a[-1]=='M':
            if b[-1]=='L':
                return False
            else:
                return True
        else:
            if b[-1]=='S':
                return len(a)<len(b)

            return False




    if a==b:
        print('=')
    elif mycomp(a,b):
        print('>')
    else:
        print('<')
