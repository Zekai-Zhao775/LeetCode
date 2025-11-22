#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param num int整型一维数组
# @return int整型二维数组
#
from typing import List


class Solution:
    def threeSum(self, num: List[int]) -> List[List[int]]:
        # write code here

        # store every two sum into dict
        # key:twosum, val:[(index, index), (index, index)]

        two_sum = {}
        for i in range(len(num)):
            for j in range(len(num)):
                s = num[i] + num[j]
                if s not in two_sum:
                    two_sum[s] = [(i, j)]
                else:
                    two_sum[s].append((i, j))

        # now, check three_sum, there will be duplicate, use a set to store result?
        result = set()
        for k in range(len(num)):
            if -num[k] in two_sum:
                for pair in two_sum[-num[k]]:
                    i, j = pair
                    if k != i and k != j and i != j:
                        abc = [num[i], num[j], num[k]]
                        abc.sort()
                        a = abc[0]
                        b = abc[1]
                        c = abc[2]
                        result.add((a, b, c))

        # transfer set to list and return
        result_list = []
        for three in result:
            a, b, c = three
            result_list.append([a, b, c])
        result_list.sort()
        return result_list