class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        for i in range(len(nums) - 2):
            # 중복 skip
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # start, end 초기값
            s, e = i + 1, len(nums) - 1

            # 남은 부분은 기존 투포인터랑 동일
            while s < e:
                if nums[i] + nums[s] + nums[e] == 0:
                    result.add((nums[i], nums[s], nums[e]))
                    s += 1
                    e -= 1
                elif nums[i] + nums[s] + nums[e] < 0:
                    s += 1
                else:
                    e -= 1

        # 중복 제거 (set?)

        return [list(x) for x in result]