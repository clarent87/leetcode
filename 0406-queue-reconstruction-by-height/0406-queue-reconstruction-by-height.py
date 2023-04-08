class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 그리디
        # 키순 정렬해서, 가장 큰것을 추출
        # k를 index로 값에 넣으면 된다함
        # sort 대신 heap 씀
        heap = []
        result = []
        for student in people:
            heapq.heappush(heap, (-student[0], student[1]))

        while heap:
            h, k = heapq.heappop(heap)
            result.insert(k, [-h, k])
        return result