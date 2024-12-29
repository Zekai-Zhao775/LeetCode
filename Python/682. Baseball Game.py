class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        score = []
        len_operations = len(operations)
        i = 0 # index of operations
        j = 0 # index of scores
        while i < len_operations:
            if operations[i] == '+':
                score.append(score[j - 1] + score[j - 2])
                j += 1
                i += 1
            elif operations[i] == 'D':
                score.append(score[j - 1] * 2)
                j += 1
                i += 1
            elif operations[i] == 'C':
                score.pop()
                j -= 1
                i += 1
            else:
                score.append(int(operations[i]))
                j += 1
                i += 1

        return sum(score)

# Optimized
class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        score = []
        for operation in operations:
            if operation == '+':
                score.append(score[-1] + score[-2])
            elif operation == 'D':
                score.append(score[-1] * 2)
            elif operation == 'C':
                score.pop()
            else:
                score.append(int(operation))
        return sum(score)

