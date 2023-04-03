from bisect import bisect_left


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        s, f = 0, 1
        while f < len(nums):
            if nums[s] == 0:
                if nums[f] != 0:
                    nums[s], nums[f] = nums[f], nums[s]
                    s += 1
                else:
                    f += 1
            else:
                s += 1
                f += 1
