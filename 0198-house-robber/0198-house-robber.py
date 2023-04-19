class Solution:
    def rob(self, nums: List[int]) -> int:
        result = defaultdict(int)

        for i in range(len(nums)):
            result[i] = max(nums[i] + result[i - 2], result[i - 1])

        return result.popitem()[1]
