class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        def dfs(i, j):
            # 제약
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return 0
            else:
                # 갔던곳은 0 세팅
                grid[i][j] = 0
                return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                result = dfs(i, j)
                if result > max_area:
                    max_area = result

        return max_area