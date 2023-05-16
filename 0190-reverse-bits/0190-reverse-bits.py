class Solution:
    def reverseBits(self, n: int) -> int:
        # 문자열 말고 이번엔 bit 연산으로 진행
        result = []
        for _ in range(32):
            result.append(str(n & 0x1))
            n = n >> 1

        return int('0b'+''.join(result),2)
