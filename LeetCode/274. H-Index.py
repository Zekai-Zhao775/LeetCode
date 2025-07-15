from collections import defaultdict
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # build a default dict
        # dict[key] = num of paper have a grater citation or equal citation than key
        # O(n*n) time and O()
        cite = defaultdict(int)
        for citation in citations:
            if not cite[citation]:
                for citation1 in citations:
                    if citation1 >= citation:
                        cite[citation] += 1
        h_index = 0
        for key in cite:
            if cite[key] >= key and key > h_index:
                h_index = key
            elif cite[key] < key and cite[key] > h_index:
                h_index = cite[key]
        return h_index