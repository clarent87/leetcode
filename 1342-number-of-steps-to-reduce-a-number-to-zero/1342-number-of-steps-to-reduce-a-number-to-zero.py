class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num > 0:
            count +=1
            if num % 2 == 0:
                num = num >> 1
            else:
                num -=1
        return count
        