class Solution:
    def countCollisions(self, directions: str) -> int:

        directions = list(directions)

        ridx = set()
        lidx = set()
        n = len(directions)
        ans = 0

        for i in range(n):
            if directions[i] == 'l':
                lidx.add(i)
            if directions[i] == 'r':
                ridx.add(i)

        nlidx = set()
        nridx = set()
        first = True

        while first or nlidx or nridx:

            ridx = ridx - nridx
            lidx = lidx - nlidx

            nlidx = set()
            nridx = set()
            for i in lidx:
                if i > 0 and directions[i - 1] != 'L':
                    directions[i] = 'S'
                    ans += 1
                    nlidx.add(i)

            for i in ridx:
                if i < n - 1 and directions[i + 1] != 'R':
                    directions[i] = 'S'
                    ans += 1
                    nridx.add(i)

            first = False
        return ans

directions = "RLRSLL"
res=Solution().countCollisions(directions)
print(res)