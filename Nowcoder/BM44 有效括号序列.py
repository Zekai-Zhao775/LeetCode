#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param s string字符串
# @return bool布尔型
#
class Solution:
    def isValid(self, s: str) -> bool:
        # write code here
        stack = []
        for c in s:
            if c == '[' or c == '(' or c == '{':
                stack.append(c)
            elif c == ']':
                if len(stack) == 0:
                    return False
                elif stack[-1] != '[':
                    return False
                elif stack[-1] == '[':
                    stack.pop()
            elif c == ')':
                if len(stack) == 0:
                    return False
                elif stack[-1] != '(':
                    return False
                elif stack[-1] == '(':
                    stack.pop()
            elif c == '}':
                if len(stack) == 0:
                    return False
                elif stack[-1] != '{':
                    return False
                elif stack[-1] == '{':
                    stack.pop()

        if len(stack) == 0:
            return True
        else:
            return False