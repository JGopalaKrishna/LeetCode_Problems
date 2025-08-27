class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dirs = [(-1, 1), (1, 1), (1, -1), (-1, -1)]
        cw = {0:1, 1:2, 2:3, 3:0}
        def iter_order(dx, dy):
            is_ = range(n) if dx > 0 else range(n-1, -1, -1)
            js_ = range(m) if dy > 0 else range(m-1, -1, -1)
            for i in is_:
                for j in js_:
                    yield i, j
        def iter_reverse(dx, dy):
            is_ = range(n-1, -1, -1) if dx > 0 else range(n)
            js_ = range(m-1, -1, -1) if dy > 0 else range(m)
            for i in is_:
                for j in js_:
                    yield i, j
        endLen = [ [ [0]*m for _ in range(n) ] for _ in range(4) ]
        stepsSinceOne = [ [ [-1]*m for _ in range(n) ] for _ in range(4) ]
        from0 = [ [ [0]*m for _ in range(n) ] for _ in range(4) ]
        from2 = [ [ [0]*m for _ in range(n) ] for _ in range(4) ]
        for d, (dx, dy) in enumerate(dirs):
            for i, j in iter_order(dx, dy):
                v = grid[i][j]
                if v == 1:
                    endLen[d][i][j] = 1
                    stepsSinceOne[d][i][j] = 0
                else:
                    pi, pj = i - dx, j - dy
                    if 0 <= pi < n and 0 <= pj < m and endLen[d][pi][pj] > 0:
                        k = stepsSinceOne[d][pi][pj]
                        need = 2 if (k + 1) % 2 == 1 else 0  # expect 2 if odd, else 0
                        if v == need:
                            endLen[d][i][j] = endLen[d][pi][pj] + 1
                            stepsSinceOne[d][i][j] = k + 1
        for d, (dx, dy) in enumerate(dirs):
            for i, j in iter_reverse(dx, dy):
                v = grid[i][j]
                ni, nj = i + dx, j + dy
                if v == 0:
                    best = 1
                    if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 2:
                        best = 1 + from2[d][ni][nj]
                    from0[d][i][j] = best
                elif v == 2:
                    best = 1
                    if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 0:
                        best = 1 + from0[d][ni][nj]
                    from2[d][i][j] = best
        ans = 0
        for d, (dx, dy) in enumerate(dirs):
            for i in range(n):
                for j in range(m):
                    t = endLen[d][i][j]
                    if t == 0: 
                        continue
                    ans = max(ans, t)
                    k = stepsSinceOne[d][i][j]
                    need_next = 2 if (k + 1) % 2 == 1 else 0
                    nd = cw[d]  # clockwise direction
                    x, y = i + dirs[nd][0], j + dirs[nd][1]
                    if 0 <= x < n and 0 <= y < m:
                        cont = from2[nd][x][y] if need_next == 2 else from0[nd][x][y]
                        ans = max(ans, t + cont)
        return ans