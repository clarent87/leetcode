class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        word = Counter()
        for r in range(1, len(s) + 1):
            word[s[r - 1]] += 1
            if word.most_common(1)[0][1] > 1:
                word[s[l]] -=1
                l += 1
        return r - l