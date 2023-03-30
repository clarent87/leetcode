class Solution:
    def reverseWords(self, s: str) -> str:
        split = s.split()
        return " ".join(x[::-1] for x in split)
