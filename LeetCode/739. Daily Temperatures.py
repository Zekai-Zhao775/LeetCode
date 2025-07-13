from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # cant be solved at O(n^2) then it will be 10^10

        answer = [0] * len(temperatures)
        print(answer)
        stack = deque()
        for i in range(len(temperatures)):
            if len(stack) == 0:
                stack.append((temperatures[i], i))
                i += 1
            elif temperatures[i] <= stack[-1][0]:
                stack.append((temperatures[i], i))
                i += 1
            else:
                while len(stack) != 0 and temperatures[i] > stack[-1][0]:
                    j = stack.pop()[1]
                    answer[j] = i - j
                stack.append((temperatures[i], i))
                i += 1

        return answer