class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        result = []
        graph = defaultdict(deque)
        for v1, v2 in sorted((tickets)):
            graph[v1].append(v2)

        def dfs(vertex: str):
            print(vertex)
            while graph[vertex]:
                dfs(graph[vertex].popleft())
            result.append(vertex)

        dfs("JFK")
        return result[::-1]