class Solution:
    def circleGame(self, toys: List[List[int]], circles: List[List[int]], r: int) -> int:

        n = len(toys)
        get_toy = set()

        for cx, cy in circles:
            for i in range(n):
                if i in get_toy:
                    continue

                tx, ty, tr = toys[i]

                if pow((cx - tx) ** 2 + (cy - ty) ** 2, 0.5) <= r - tr:
                    get_toy.add(i)

        return len(get_toy)