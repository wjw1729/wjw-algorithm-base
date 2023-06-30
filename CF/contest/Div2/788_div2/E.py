# ---------------------------------------- fast io ----------------------------------------
import os, sys
from io import BytesIO, IOBase

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
# ---------------------------------------- fast io ----------------------------------------


from collections import deque,defaultdict
def constructTree(edges):
    root=edges[0][0]

    value=[0]*(2**p+1)

    value[root]=2**p

    edv=[0]*len(edges)
    indexmap={tuple(sorted(c)):i for i,c in enumerate(edges)}


    child=defaultdict(list)
    q=deque()
    q.append(root)
    g=[[] for _ in range(2**p+1)]
    for u,v in edges:
        g[u].append(v)
        g[v].append(u)

    vis=set()
    vis.add(root)

    while q:
        u=q.popleft()

        for v in g[u]:
            if v not in vis:
                child[u].append(v)
                q.append(v)
                vis.add(v)

    als=[]
    for i in range(1,2**p):
        als.append((i,i+2**p))


    q=deque()
    q.append(root)

    while q:
        u=q.popleft()

        for v in child[u]:
            tmp=als.pop()
            if value[u]&(1<<p):
                edv[indexmap[tuple(sorted([u,v]))]]=tmp[1]
                value[v]=tmp[0]
            else:
                edv[indexmap[tuple(sorted([u, v]))]] = tmp[0]
                value[v] = tmp[1]
            q.append(v)

    return root,value,edv





t=int(input())

for _ in range(t):
    p=int(input())
    edges=[]
    for _ in range(2**p-1):
        edges.append([int(x) for x in input().split()])

    res=constructTree(edges)

    print(res[0])
    print(*res[1][1:])
    print(*res[2])



