from collections import Counter

str='aaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'
d=Counter(str)
x=min(d.keys())
res=d[min(d.keys())]
print(res)

print('a'>'b')