class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket == "(" or bracket == "{" or bracket == "[":
                stack.append(bracket)
            elif len(stack) == 0:
                return False
            elif bracket == ")" and stack[-1] != "(":
                return False
            elif bracket == "}" and stack[-1] != "{":
                return False
            elif bracket == "]" and stack[-1] != "[":
                return False
            else:
                stack.remove(stack[-1])
        return True if len(stack) == 0 else False