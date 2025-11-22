class Interval:
    def __init__(self, a=0, b=0):
        self.start = a
        self.end = b
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param intervals Interval类一维数组
# @return Interval类一维数组
#
from typing import List


class Solution:
    def merge(self , intervals: List[Interval]) -> List[Interval]:
        # write code here
        # sort itervals first, O(nlog(n))
        intervals.sort(key = lambda x: x.start)
        result = []
        for iterval in intervals:
            if result == []:
                result.append(iterval)
            else:
                if iterval.start > result[-1].end:
                    result.append(iterval)
                elif iterval.start == result[-1].end:
                    result[-1].end = iterval.end
                elif iterval.start < result[-1].end:
                    if iterval.end > result[-1].end:
                        result[-1].end = iterval.end
        return result