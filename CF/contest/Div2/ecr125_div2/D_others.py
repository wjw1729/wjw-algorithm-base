import io, os
import bisect

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def main(t):
    n, C = map(int, input().split())
    dic = [0] * (C + 1)

    for i in range(n):
        ci, di, hi = map(int, input().split())
        dic[ci] = max(dic[ci], di * hi)

    arr = [0] * (C + 1)

    for key in range(C + 1):
        if dic[key] == 0: continue
        i = key
        num = dic[key]
        while i <= C:
            arr[i] = max(arr[i], num)
            num += dic[key]
            i += key

    for i in range(1, C + 1):
        arr[i] = max(arr[i - 1], arr[i])

    m = int(input())
    ans = []

    for i in range(m):
        Di, Hi = map(int, input().split())
        num = Di * Hi
        if num >= arr[-1]:
            ans.append(-1)
        else:
            loc = bisect.bisect(arr, num)
            ans.append(loc)

    ans = " ".join(map(str, ans))

    print(ans)


T = 1  # int(input())
t = 1
while t <= T:
    main(t)
    t += 1
