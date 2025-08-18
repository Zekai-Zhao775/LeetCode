from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = defaultdict(list)
        poped = set()
        for s in strs:
            strs_dict["".join(sorted(s))].append(s)
        result = []
        for key in strs:
            if "".join(sorted(key)) not in poped:
                result.append(strs_dict["".join(sorted(key))])
                poped.add("".join(sorted(key)))
        return result