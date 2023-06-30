n = int(input())
s = input()

num0 = s.count('0')
num1 = len(s) - num0

ans = list(range(2 ** num1, 2 ** n - (2 ** num0 - 1) + 1))
print(*ans)
