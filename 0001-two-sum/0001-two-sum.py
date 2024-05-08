# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         pf, pe = 0, len(nums) - 1
#         tmp = list()

#         for i, v in enumerate(nums):
#             tmp.append((i,v))

#         tmp.sort(key=lambda x: x[1])
#         while pf < pe:
#             sum = tmp[pf][1] + tmp[pe][1]
#             if sum == target:
#                 return [tmp[pf][0], tmp[pe][0]]
#             elif sum > target:
#                 pe -= 1
#             else:  # target보다 sum이 작음
#                 pf += 1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """풀이
        1. 이중 반복.
        2. hash
        """
        # 1. dict 만들기
        map = dict(zip(nums, range(len(nums))))

        # 2. 빼서 구하기
        for i, e in enumerate(nums):
            index = target - e
            if index in map and map[index] is not i:
                return [i, map[index]]