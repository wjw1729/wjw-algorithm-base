a=[int(x) for x  in input().split()]
x=int(input())
print(*[max(x-y,0) for y in a])