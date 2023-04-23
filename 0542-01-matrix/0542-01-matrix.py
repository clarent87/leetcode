class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # bfs로 진행.
        # 1) 큐에 진입점 추가
        q = deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = -1

        # 2) 루프 돌면서 진행필요, tric (안간곳을 -1 마킹, 원래는 visit list,dic 활용..)
        #    값 세팅.
        loop = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            i, j = q.popleft()
            for r, c in loop:
                ir, jc = i + r, j + c
                if ir < 0 or ir >= len(mat) or jc < 0 or jc >= len(mat[0]) or mat[ir][jc] != -1:
                    continue
                mat[ir][jc] = mat[i][j] + 1
                q.append((ir,jc))
        return mat