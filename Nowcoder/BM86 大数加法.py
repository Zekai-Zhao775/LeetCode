#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 计算两个数之和
# @param s string字符串 表示第一个整数
# @param t string字符串 表示第二个整数
# @return string字符串
#
class Solution:
    def solve(self, s: str, t: str) -> str:
        # write code here
        # return str(int(s) + int(t))
        s_list = []
        t_list = []
        result_list = []

        for i in range(len(s)):
            s_list.append(int(s[i]))
        for i in range(len(t)):
            t_list.append(int(t[i]))

        carry = 0
        while s_list != [] and t_list != []:
            a = s_list.pop()
            b = t_list.pop()
            result_list.append(str((a + b + carry) % 10))
            if a + b + carry >= 10:
                carry = 1
            else:
                carry = 0
        remain = []
        if s_list != []:
            remain = s_list
        elif t_list != []:
            remain = t_list

        while remain != []:
            a = remain.pop()
            result_list.append(str((a + carry) % 10))
            if a + carry >= 10:
                carry = 1
            else:
                carry = 0

        if carry == 1:
            result_list.append(str(carry))
        result_list.reverse()
        return "".join(result_list)