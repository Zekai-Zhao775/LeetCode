class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapping = {}
        mapping_value = set()
        j = 0
        j_last = 0
        for i in range(len(pattern)):
            while j < len(s) and s[j] != " ":
                j += 1
            word = s[j_last:j]
            j += 1
            j_last = j
            if pattern[i] not in mapping:
                if word in mapping_value:
                    return False
                mapping[pattern[i]] = word
                mapping_value.add(word)
            elif pattern[i] in mapping:
                if mapping[pattern[i]] != word:
                    return False
        if j != len(s) + 1:
            return False
        return True