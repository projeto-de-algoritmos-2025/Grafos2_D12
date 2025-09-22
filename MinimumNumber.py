from typing import List

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def count_islands():
            visited = set()
            islands = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and (i, j) not in visited:
                        islands += 1
                        stack = [(i, j)]
                        visited.add((i, j))
                        while stack:
                            r, c = stack.pop()
                            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                                nr, nc = r + dr, c + dc
                                if 0 <= nr < m and 0 <= nc < n and \
                                   grid[nr][nc] == 1 and (nr, nc) not in visited:
                                    visited.add((nr, nc))
                                    stack.append((nr, nc))
            return islands

        if count_islands() != 1:
            return 0

        land_cells = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    land_cells.append((i, j))

        for i, j in land_cells:
            grid[i][j] = 0  
            if count_islands() != 1:
                return 1
            grid[i][j] = 1  

        return 2

