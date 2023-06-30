


t=int(input())

for _ in range(t):
    s=input()

    res=(ord(s[0])-ord('a'))*25
    res+=ord(s[1])-ord('a')-(1 if s[0]<s[1] else 0)+1
    print(res)