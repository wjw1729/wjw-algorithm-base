
n=int(input())
s=input()


def solve():
    if s[0]=='A' and s[-1]=='B':
        return False
    if s=='BA':
        return False

    return True

if solve():
    print('Yes')
else:
    print('No')
