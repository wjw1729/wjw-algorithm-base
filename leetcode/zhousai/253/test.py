from sortedcontainers import SortedDict

a=SortedDict()
a[1]=2
a[2]=1
a[0]=5
print(list(a.keys()))