#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 验证IP地址
# @param IP string字符串 一个IP地址字符串
# @return string字符串
#
class Solution:
    def solve(self , IP: str) -> str:
        # write code here
        if '.' in IP:
            temp = []
            count = 0
            for i in range(len(IP)):
                if IP[i] >= '0' and IP[i] <= '9':
                    if temp == [] and IP[i] == '0':
                        return "Neither"
                    else:
                        temp.append(IP[i])
                        if len(temp) > 3:
                            return "Neither"
                elif IP[i] == '.':
                    if i == 0 or i == len(IP) - 1 or IP[i - 1] == '.':
                        return "Neither"
                    temp_num = (int)("".join(temp))
                    if temp_num > 255:
                        return "Neither"
                    temp = []
                    count += 1
                else:
                    return "Neither"
            if temp != []:
                temp_num = (int)("".join(temp))
                if temp_num > 255:
                    return "Neither"
                count += 1
            if count > 4:
                return "Neither"
            return "IPv4"
        elif ':' in IP:
            temp = []
            count = 0
            for i in range(len(IP)):
                # 10 a, 11 b, 12 c, 13 d, 15 e
                if (IP[i] >= '0' and IP[i] <= '9') or (IP[i] >= 'a' and IP[i] <= 'e') or (IP[i] >= 'A' and IP[i] <= 'E'):
                    temp.append(IP[i])
                    if len(temp) > 4:
                        return "Neither"
                elif IP[i] == ':':
                    if i == 0 or i == len(IP) - 1 or IP[i - 1] == ':':
                        return "Neither"
                    if temp == []:
                        return "Neither"
                    temp = []
                    count += 1
                else:
                    return "Neither"
            if temp != []:
                count += 1
            if count > 8:
                return "Neither"
            return "IPv6"
        return "Neither"