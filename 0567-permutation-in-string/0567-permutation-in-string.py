class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        s = 0

        for e in range(1,len(s2)+1 ):
            if s2[e-1] in s1_count:
                s1_count[s2[e - 1]] -= 1

            # 종료 조건 계산.
            if s1_count.most_common(1)[0][1] == 0:
                return True

            # 윈도우 슬라이딩
            if e - s == len(s1):
                if s2[s] in s1_count:
                    s1_count[s2[s]] += 1
                s += 1

        return False