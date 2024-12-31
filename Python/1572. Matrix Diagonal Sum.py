class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        sum = 0
        len_mat = len(mat)
        i = 0

        for row in mat:
            sum += row[i] + row[len_mat - 1 - i]
            i += 1
        if len_mat % 2 == 0:
            return sum
        else:
            return sum - mat[len_mat / 2][len_mat / 2]