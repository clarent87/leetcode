class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        stack = []  # 현재 완성된 문자.

        def bt(index: int):
            if index == len(s):
                result.append("".join(stack))
                return 
            if s[index].isalpha():
                stack.append(s[index].lower())
                bt(index + 1)
                stack.pop()

                stack.append(s[index].capitalize())
                bt(index + 1)
                stack.pop()
            else:
                stack.append(s[index])
                bt(index + 1)
                stack.pop()

        bt(0)

        return result
