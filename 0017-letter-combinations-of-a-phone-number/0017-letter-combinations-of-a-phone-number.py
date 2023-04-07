class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        pad = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
               "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        result = []

        def dfs(i: int, path: str):
            if len(path) == len(digits):
                result.append(path)
                return
            for word in pad[digits[i]]:
                dfs(i + 1, path + word)

        if not digits:
            return []
        
        dfs(0, "")

        return result
