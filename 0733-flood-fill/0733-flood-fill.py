class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        init_color = image[sr][sc]
        def dfs(i: int, j: int):

            if i < 0 or i >= len(image) \
                    or j < 0 or j >= len(image[0]) \
                    or image[i][j] != init_color:
                return

            image[i][j] = color

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        
        if image[sr][sc] != color:
            dfs(sr, sc)

        return image