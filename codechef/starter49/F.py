from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]


    def solve():
        cnt = Counter(a)

        d = set()
        kls = sorted(cnt.keys())
        m = len(kls)
        for i in range(m):
            for j in range(i + 1, m):
                d.add(abs(kls[j] - kls[i]))

        tag = [1] * m
        res = 0
        for i, (k, v) in enumerate(sorted(cnt.items())):
            if v > 1:
                tag[i] = v
                res += v

        for ddd in d:

            def get(d, tag):
                idxmap = {c: i for i, c in enumerate(kls)}

                flag = [False] * m
                res = 0

                for i, (k, v) in enumerate(sorted(cnt.items())):
                    if not flag[i]:
                        tc = tag[i] > 1
                        tmp = v

                        while k + d in idxmap:
                            if tag[idxmap[k + d]] > 1:
                                tc = True

                            k = k + d
                            flag[idxmap[k]] = True
                            tmp += cnt[k]
                        if tc:
                            res += tmp
                        else:
                            res += tmp // 2 * 2

                return res

            res = max(res, get(ddd, tag[:]))

        return res


    print(solve())
