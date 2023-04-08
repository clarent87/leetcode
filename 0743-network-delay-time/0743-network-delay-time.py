class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 인접 리스트로 그래프 구성
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # 다익스트라 각 노드까지 거리
        dist = defaultdict(int)

        # 다음에 갈 노드 추가
        # bfs의 큐, 단 여기서는 다음 노드를 weight로 선 ( 즉 최단거리로 선택 )
        Q = [(0, k)]

        # bfs 구현
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time  # 다익스트라 였다면 이건 없음
                for v, w in graph[node]:  # 다음 노드들 추가
                    # 다음 최소 경로 뽑아야 해서 time+w로 추가
                    # heap 안썻다면, Q list에 append 후 전체 순회해서 다음 노드를 뽑아야함.

                    # 다익스트라 였다면 여기에서 dist 업데이트 진행.
                    # point
                    # v2가 큐에 있지만 만약 현재 v2로 가는 거리가 짧으면 큐에 들어가서 이게 처리됨
                    # 그럼 남은 v2는 이미 방문했다해서 다시 프로세싱되진 않음
                    heapq.heappush(Q, (time + w, v))


        if len(dist) == n:
            return max(dist.values())
        return -1