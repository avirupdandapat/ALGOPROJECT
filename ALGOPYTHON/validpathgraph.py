class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : list of integers
    # @param F : list of integers
    # @return a strings
    def solve(self, x, y, N, R, A, B):
        def inside_circle(r, x, y, xs, ys, n):
            for i in range(n):
                if ((xs[i] - x) ** 2 + (ys[i] - y) ** 2) ** 0.5 <= r:
                    return True
            return False

        q = [(0, 0)]
        visited = set()
        visited.add((0, 0))
        dire = [(-1, -1), (-1, 0), (0, -1), (-1, 1), (1, -1), (0, 1), (1, 0), (1, 1)]

        while q:
            cx, cy = q.pop(0)
            if cx == x and cy == y: return 'YES'
            for dx, dy in dire:
                if 0 <= cx + dx <= x and 0 <= cy + dy <= y and not inside_circle(R, cx + dx, cy + dy, A, B, N) and (
                cx + dx, cy + dy) not in visited:
                    q.append((cx + dx, cy + dy))
                    visited.add((cx + dx, cy + dy))
        return 'NO'

