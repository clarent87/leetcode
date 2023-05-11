class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        memo = [[-1] * len(n) for n in triangle]
        max_level = len(triangle)-1

        def min_path(index: int, level: int) -> int:
            if level == max_level:
                return triangle[level][index]
            if memo[level][index] != -1:
                return memo[level][index]

            memo[level][index] = triangle[level][index] + min(min_path(index, level + 1), min_path(index + 1, level + 1))
            return memo[level][index]

        return min_path(0, 0)