x, y = [int(x) for x in input().split()]

els = [y, y, y]
ans = 0
while els != [x, x, x]:
    if els[0] + els[1] - 1 >= x:
        ans += 3
        break
    else:
        els[2] = els[0] + els[1] - 1
        ans += 1
    els.sort(reverse=True)

print(ans)
