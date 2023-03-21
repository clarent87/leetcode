def my_sum(count: int):
    return int((1 + count) * count / 2)
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count_list = []
        count = 0
        sum = 0
        for x in nums:
            if x == 0:
                count += 1
            else:
                count_list.append(count)
                count = 0
        else:
            count_list.append(count)

        for x in count_list:
            sum += my_sum(x)
        return sum

