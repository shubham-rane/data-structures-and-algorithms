class Solution:
    def isValid(self, s: str) -> bool:
        stack  = []
        for char in s:
            if char == "(":
                stack.append(")")
            elif char == "{":
                stack.append("}")
            elif char == "[":
                stack.append("]")
            else: 
                if len(stack) == 0:
                    return False
                if char == stack[-1]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        return False
        