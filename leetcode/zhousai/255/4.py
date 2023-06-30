import collections
class Solution:
    def recoveryArray(self, n, sums):
        def remove_v(nt, t):
            assert t >= 0
            to_remove = collections.Counter()
            small = []
            large = []
            for v in nt:
                if to_remove[v] > 0:
                    to_remove[v] -= 1
                    continue
                small.append(v)
                large.append(v + t)
                to_remove[v + t] += 1
            if not len(small) * 2 == len(nt):
                return None, None

            return small, large

        def solve(n=n, sums=sums):
            if n == 1:
                return [sums[1]] if sums[0] == 0 else [sums[0]]

            sums = sorted(sums)
            t = sums[-1] - sums[-2]
            # 要么存在t，要么存在-t
            small, large = remove_v(sums, t)
            if small is None:
                return None

            if t in sums:
                t1 = solve(n - 1, small)
                if not t1 is None:
                    return [t] + t1
            if -t in sums:
                t1 = solve(n - 1, large)
                if not t1 is None:
                    return [-t] + t1
            return None

        return solve()
