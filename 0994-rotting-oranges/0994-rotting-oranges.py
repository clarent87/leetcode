class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 초기 진입 위치 추가
        ## targets는 방문해야 하는 위치
        targets, start = set(), deque()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    start.append((i, j))
                elif grid[i][j] == 1:
                    targets.add((i, j))
        # bfs
        ## vist 두는게 나음
        ## 마지막 남은 것은 visit가 없음. 즉 단계를 진행할 필요가 없어서 and targets 필요
        result = 0
        while start and targets:
            for _ in range(len(start)):
                i, j = start.popleft()
                for r, c in {(0, 1), (0, -1), (1, 0), (-1, 0)}:
                    ir, jc = i + r, j + c
                    # if ir < 0 or ir >= m or jc < 0 or jc >= n or (ir, jc) not in targets: 이런 조건은 BFS에서는 필요가 없음
                    #     continue
                    if (ir, jc) in targets:
                        start.append((ir, jc))
                        targets.remove((ir, jc))
            result += 1

        return -1 if targets else result