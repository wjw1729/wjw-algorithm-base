import bisect

l1=list(range(100))
idx=bisect.bisect_left(l1,55)
print(idx)