# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n

        while start <= end:
            mid = (start + end) // 2
            if isBadVersion(mid) is True:
                if mid == 1:
                    return mid
                if mid-1 >=1 and isBadVersion(mid-1) is False:
                    return mid
                else:
                    end = mid - 1
            else:
                start = mid + 1
