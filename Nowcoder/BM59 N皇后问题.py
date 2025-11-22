#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param n int整型 the n
# @return int整型
#
class Solution:
    def Nqueen(self , n: int) -> int:
        # write code here
        # 对角线 diagonal
        # for positive diagonal, always r - c = a
        # for negative diagonal, always r + c = a
        cols = set() # 列
        diag_p = set()
        diag_n = set()
        count = 0
        def backtrack(r):
            nonlocal count
            if r == n:
                count += 1
                return
            for c in range(n):
                if c not in cols and r - c not in diag_p and r + c not in diag_n:
                    cols.add(c)
                    diag_p.add(r - c)
                    diag_n.add(r + c)
                    backtrack(r + 1)
                    cols.remove(c)
                    diag_p.remove(r - c)
                    diag_n.remove(r + c)
        backtrack(0)
        return count