class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 조합, 순열의 기본 형을 익혀야 할듯
        result = []

        def bt(start: int, path: list):
            result.append(path)
            for i in range(start, len(nums)):
                bt(i+1, path + [nums[i]])

        bt(0, [])
        return result
