class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        volumn = 0

        if len(height) == 0:
            return 0

        # 스택에다가 index를 넣어야 함.
        # 오른쪽을 기준으로 왼쪽보다 높다면 물을 채운다는 느낌으로..
        # 채울 물은 왼쪽 오른쪽 중 낮은 쪽에 의존.

        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                # 바로앞 block을 얼마로 채울지를 결정.
                # 의미상 바로 앞인데, 실제로는 바로 앞일지 몇단계 더 전일진 알수 없음.
                base_block = stack.pop()

                # 남은 block이 없다면 break
                if not stack:
                    break

                # base_block 양옆 장벽을 기준으로 사이의 거리를 계산
                # stack에 block과의 거리를 계산
                distance = i - stack[-1] -1

                # 높이 차이 계산 ( 한개 단위 ) , 양 장벽중 낮은 위치 로 계산
                water_unit = min(height[stack[-1]], height[i]) - height[base_block]

                volumn += water_unit * distance

            # 앞전 block보다 높이가 낮다면 stack에 추가
            stack.append(i)

        return volumn