class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError: # 값이 없으면 에러 나서.. 예외 처리 해줌
            return -1