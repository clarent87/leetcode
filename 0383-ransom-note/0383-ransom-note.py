class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)
        answer = ransom_count - magazine_count
        
        return all( not x for x in answer.values())
