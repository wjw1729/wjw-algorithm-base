import itertools


nums=[1,2,3,4]
x=itertools.combinations(nums,1)
x=list(x)

y=[list(m) for m in x]
print(1)