class Solution:
    def candy(self, ratings: List[int]) -> int:
        result = [1 for _ in ratings]
        # -->
        for i in range(1, len(ratings)):
            if ratings[i-1] < ratings[i] and result[i] <= result[i - 1]:
                result[i] = result[i-1] + 1

        # <--
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and result[i] <= result[i + 1]:
                result[i] = result[i+1] + 1
        return sum(result)