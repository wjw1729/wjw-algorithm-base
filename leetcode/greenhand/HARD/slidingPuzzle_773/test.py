a=[1,2,3,4,5]
d=tuple(a)
b=(1)
c=set()
c.add(d)
c.add(b)
print(a in c)