class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        _, max_count = counter.most_common(1)[0]

        # 마지막 줄의 갯수를 계산해야함
        # 1. most_common의 갯수보다 작은 것들 몇 개인지 확인
        remain_count = 0
        for _, count in counter.most_common():
            if count == max_count:
                remain_count += 1
        # 2. n+1 - 위 갯수.
        return max((n + 1) * (max_count - 1) + remain_count, len(tasks))