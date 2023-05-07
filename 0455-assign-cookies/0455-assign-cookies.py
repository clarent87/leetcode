class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        if not s:
            return 0

        g.sort()
        s.sort()
        # 그리디 하게 푼다면 s 만큼 돌면서 check.
        g_i, s_i = 0, 0
        while g_i < len(g) and s_i < len(s):
            # 쿠키를 줄수 있다 (g_i)아이에게
            if s[s_i] >= g[g_i]:
                g_i += 1
            s_i += 1
                
        return g_i