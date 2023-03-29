class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        ans = list()

        while l <= r:
            squares_l = nums[l] ** 2
            squares_r = nums[r] ** 2
            if squares_l >= squares_r:
                ans.append(squares_l)
                l += 1
            else:
                ans.append(squares_r)
                r -= 1

        return ans[::-1]