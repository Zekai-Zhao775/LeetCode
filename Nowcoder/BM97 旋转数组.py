#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 旋转数组
# @param n int整型 数组长度
# @param m int整型 右移距离
# @param a int整型一维数组 给定数组
# @return int整型一维数组
#
from typing import List


class Solution:
    def solve(self, n: int, m: int, a: List[int]) -> List[int]:
        # write code here
        # O(1) space
        # 每个数字以m为gap移动，回到原点结束
        # 对前最大公因数个数字移动

        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        for i in range(gcd(n, m)):
            last = a[i]
            j = (i + m) % n
            while j != i:
                temp = a[j]
                a[j] = last
                last = temp
                j = (j + m) % n
            a[j] = last

        return a