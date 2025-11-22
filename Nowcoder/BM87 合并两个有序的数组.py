
#
#
# @param A int整型一维数组
# @param B int整型一维数组
# @return void
#
class Solution:
    def merge(self , A, m, B, n):
        # write code here
        C = []
        i = 0
        j = 0
        while i < m and j < n:
            if A[i] <= B[j]:
                C.append(A[i])
                i += 1
            elif A[i] > B[j]:
                C.append(B[j])
                j += 1
        if i == m and j == n:
            for k in range(m + n):
                A[k] = C[k]
            return
        else:
            if i == m:
                while j < n:
                    C.append(B[j])
                    j += 1
            elif j == n:
                while i < m:
                    C.append(A[i])
                    i += 1
        for k in range(m + n):
            A[k] = C[k]
        return