from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # n = 10^5
        # must be O(nlog(n)) or O(n)

        # use dict, around O(3n)
        r_dict = defaultdict(int)
        m_dict = defaultdict(int)
        for c in ransomNote:
            r_dict[c] += 1
        for c in magazine:
            m_dict[c] += 1
        for c in ransomNote:
            if c not in m_dict or r_dict[c] > m_dict[c]:
                return False
        return True