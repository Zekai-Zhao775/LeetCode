class Solution:
    def decodeString(self, s: str) -> str:
        # stack
        k = 0  # current number to repeat
        countStack = []  # stack holding k
        current = ''  # string for the current level
        stringStack = []  # stack holding current

        for char in s:
            if char.isdigit():
                k = k * 10 + int(char)
            elif char == '[':
                countStack.append(k)
                k = 0
                stringStack.append(current)
                current = ''
            elif char == ']':
                current = stringStack.pop() + countStack.pop() * current
            else:
                current += char

        return current

# class Solution:
#     def decodeString(self, s: str) -> str:
#         # recursive
#         print(s)
#         sListEncoded = []
#         sListDecoded = []
#         sEncoded = []
#         leftFlag = 0
#         rightFlag = 0
#         for char in s:
#             if char == '[':
#                 sEncoded.append(char)
#                 leftFlag += 1
#             elif char ==']':
#                 sEncoded.append(char)
#                 rightFlag += 1
#                 if leftFlag == rightFlag:
#                     # store n[abc]
#                     sListEncoded.append(''.join(sEncoded))
#                     sEncoded = []
#                     leftFlag = 0
#                     rightFlag = 0
#             elif char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
#                 if leftFlag == 0 and rightFlag == 0 and all(c.isalpha() for c in sEncoded):
#                     sListEncoded.append(''.join(sEncoded))
#                     sEncoded = []
#                 sEncoded.append(char)
#             else:
#                 sEncoded.append(char)
#         if sEncoded != []:
#             sListEncoded.append(''.join(sEncoded))

#         print(sListEncoded)

#         for s in sListEncoded:
#             print(s)
#             # if no [] in s, s is 'abc'
#             if s.count(']') == 0:
#                 sListDecoded.append(s)
#             # if only one [] in s (core logic)
#             # aa2[aa]
#             elif s.count(']') == 1:
#                 num = []
#                 sDecoded = []
#                 for char in s:
#                     if char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
#                         num.append(char)
#                     elif char != '[' and char != ']':
#                         sDecoded.append(char)
#                 num = int(''.join(num))
#                 sDecoded = (''.join(sDecoded)) * num
#                 sListDecoded.append(sDecoded)
#             # more than one [] in s, and in '3[a2[c]]' format, remove the out number and []
#             else:
#                 sInside = []
#                 start = 0
#                 stop = 0
#                 num = []
#                 for char in s:
#                     print("char = ", char)
#                     # print("start = ", start)
#                     # print("stop = ", stop)
#                     if start == 0 and char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
#                         num.append(char)

#                     if char == '[':
#                         start += 1
#                     elif char == ']':
#                         stop += 1

#                     if start != 0:
#                         sInside.append(char)
#                     if start != 0 and start == stop:
#                         break
#                 num = int(''.join(num))
#                 sInside = ''.join(sInside[1:-1]) # remove the outer []
#                 print("sInside = ", sInside)
#                 sListDecoded.append(num * (self.decodeString(sInside)))

#         return ''.join(sListDecoded)