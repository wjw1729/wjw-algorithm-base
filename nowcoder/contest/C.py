from collections import  defaultdict
def compute(s1,s):
    if len(s1)!=len(s):
        return 0

    return sum(s1[i]==s[i] for i in range(len(s)))



s=input()
n=int(input())

d=defaultdict(list)
for i in range(n):
    s1=input()
    d[compute(s1,s)].append(s1)


sls=sorted(d.items(),key=lambda x:(-x[0],x[1]))

for c in sls[0][1]:
    print(c)




