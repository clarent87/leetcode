class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mx = tmp = 0
        for i in nums:
            if i == 1:
                tmp+=1
            else :
                mx = max(mx,tmp)
                tmp = 0
        return max(mx, tmp)
        