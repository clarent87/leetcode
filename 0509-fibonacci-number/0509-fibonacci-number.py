class Solution:
    dp = defaultdict(int)
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        if self.dp[n] > 0:
            return self.dp
        return self.fib(n-1) + self.fib(n-2)
