class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def dfs(element: list, index: int, my_sum: int):
            for i in range(index, len(candidates)):
                current_sum = candidates[i] + my_sum
                element.append(candidates[i])

                if current_sum < target:
                    dfs(element,i, current_sum)
                elif current_sum == target:
                    result.append(element[:])
                element.pop()

        dfs([], 0, 0)

        return result