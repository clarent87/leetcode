class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def bt(start: int, countdown: int, path):
            if countdown == 0:
                result.append(path)
            for x in range(start, n+1):
                bt(x + 1, countdown - 1, path + [x])

        bt(1, k, [])
        return result