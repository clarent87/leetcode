class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pf, pe = 0, len(nums) - 1
        tmp = list()

        for i, v in enumerate(nums):
            tmp.append((i,v))

        tmp.sort(key=lambda x: x[1])
        while pf < pe:
            sum = tmp[pf][1] + tmp[pe][1]
            if sum == target:
                return [tmp[pf][0], tmp[pe][0]]
            elif sum > target:
                pe -= 1
            else:  # target보다 sum이 작음
                pf += 1
