class Solution:
    def simplifyPath(self, path: str) -> str:
        # edge
        if len(path) == 2:
            if path == "//":
                return "/"
            elif path == "/.":
                return "/"

        # remove duplicate / O(n)
        result = []
        for c in path:
            result.append(c)
        i = 1
        while i < len(result):
            if result[i] == '/' and result[i - 1] == '/':
                result.pop(i)
            else:
                i += 1

        # remove last /
        if result[-1] == '/':
            result.pop()

        stack = []
        i = 0
        while i < len(result):
            if result[i] == '/':
                i += 1
                current = i
                while i < len(result) and result[i] != '/':
                    i += 1
                if "".join(result[current:i]) == '..':
                    if len(stack) != 0:
                        stack.pop()
                elif "".join(result[current:i]) == '.':
                    continue
                else:
                    stack.append("".join(result[current:i]))
        result_return = []
        if len(stack) == 0:
            result_return.append('/')
        for item in stack:
            result_return.append('/')
            result_return.append(item)

        # print(result)
        return "".join(result_return)