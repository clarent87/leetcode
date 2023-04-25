class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        visit = set()
        visited = set() # 최적화용 ( 아래와 같은 경우 3->4는 다시 방문 안해도 되게 )
                        # 1 -> 2 -> 3 -> 4
                        # 1 -> 5 -> 3 -> 4

        def dfs(a: int) -> bool:
            # 방문한 적이 있으면
            if a in visited:
                return True # 사이클이 생긴경우는 False 로 로직이 종료되므로, 그렇지 않은경우는 True
            # 사이클 있으면
            if a in visit:
                return False
            # 방문 세팅
            visit.add(a)
            for b in graph[a]:
                if not dfs(b):
                    return False
            # 현단계 종료/초기화
            visit.remove(a)
            # 방문 완료
            visited.add(a)
            return True

        for a in list(graph):
            if not dfs(a):  # 사이클이 있으면
                return False

        return True