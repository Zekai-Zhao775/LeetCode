class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Just use lower()
        # return lower(s)

        # ASCII value ord()
        gap = ord('A') - ord('a')
        ascii_A = ord('A')
        ascii_Z = ord('Z')
        result = []

        for char in s:
            # if ord(char) >= ascii_A and ord(char) <= ascii_Z:
            if 'A' <= char <= 'Z':
                result.append(chr(ord(char) - gap))
            else:
                result.append(char)

        return ''.join(result)