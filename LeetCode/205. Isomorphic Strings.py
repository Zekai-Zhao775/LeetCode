class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapping = {}
        mapping_value = set()
        for i in range(len(s)):
            if s[i] in mapping:
                if mapping[s[i]] != t[i]:
                    return False
            elif s[i] not in mapping:
                if t[i] in mapping_value:
                    return False
                mapping[s[i]] = t[i]
                mapping_value.add(t[i])
            i += 1
        return True