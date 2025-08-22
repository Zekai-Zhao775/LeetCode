class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            stack.append(c)
            if len(stack) >= 2:
                while len(stack) >= 2:
                    if stack[-2] == '(' and stack[-1] == ')':
                        stack.pop()
                        stack.pop()
                    elif stack[-2] == '{' and stack[-1] == '}':
                        stack.pop()
                        stack.pop()
                    elif stack[-2] == '[' and stack[-1] == ']':
                        stack.pop()
                        stack.pop()
                    else:
                        break

        if len(stack) != 0:
            return False
        else:
            return True