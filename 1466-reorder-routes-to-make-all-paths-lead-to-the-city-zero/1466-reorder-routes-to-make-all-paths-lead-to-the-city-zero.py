class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        city_map = defaultdict(deque)
        for x, y in connections:
            city_map[x].append((x, y))
            city_map[y].append((x, y))
        return self.sub_solution(0, -1, city_map)

    def sub_solution(self, n: int, parent: int, city_map: Dict[int, deque[set]]) -> int:
        count = 0
        while city_map[n]:
            a, b = city_map[n].popleft()

            # 다음 city로 이동
            if n == a and b != parent:
                count += self.sub_solution(b, n, city_map) + 1

            # 현재 city로 오는 길
            elif n == b and a != parent:
                count += self.sub_solution(a, n, city_map)
        return count
