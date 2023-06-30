class Solution:
    def minRemainingSpace(self, N, V: int) -> int:
            n = len(N)
            f = [0] * (V + 1)

            for i in range(n):
                for j in range(V, -1, -1):
                    if j >= N[i]:
                        f[j] = max(f[j], f[j - N[i]] + N[i])

            return V-f[V]