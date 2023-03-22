class Solution:

    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = self.make_dict(roads)
        queue = deque(graph[1])
        del graph[1]
        min = float('inf')

        while len(queue) != 0:
            b, dist = queue.popleft()
            if dist < min:
                min = dist
            queue += deque(graph[b])
            del graph[b]
        return min

    def make_dict(self, roads: List[List[int]]) -> Dict:
        graph = defaultdict(list)
        for x in roads:
            graph[x[0]].append((x[1], x[2]))
            graph[x[1]].append((x[0], x[2]))
        return graph