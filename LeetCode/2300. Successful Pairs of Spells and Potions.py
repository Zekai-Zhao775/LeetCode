from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # sort potions O(nlogn)
        potions.sort()

        # print("potions = ", potions)

        # binary search O(logn)
        def successfulPairsPerSpell(spell: int) -> int:
            # print("----------")
            # print("spell = ", spell)
            start = 0
            end = len(potions) - 1
            while start < end:
                middle = (start + end) // 2
                score = spell * potions[middle]
                # print("start = ", start)
                # print("middle = ", middle)
                # print("end = ", end)
                # print("score = ", score)
                # print("-")
                if score >= success:
                    end = middle - 1
                elif score < success:
                    start = middle + 1

            score = spell * potions[start]
            if score >= success:
                return len(potions) - start
            else:
                return len(potions) - start - 1

        result = []
        for spell in spells:
            result.append(successfulPairsPerSpell(spell))
        return result