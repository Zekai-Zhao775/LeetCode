from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = []
        for bill in bills:
            if bill == 5:
                change.append(5)
            elif bill == 10:
                if 5 in change:
                    change.remove(5)
                    change.append(10)
                else:
                    return False
            elif bill == 20:
                if 10 in change and 5 in change:
                    change.remove(10)
                    change.remove(5)
                    change.append(20)
                elif change.count(5) >= 3:
                    change.remove(5)
                    change.remove(5)
                    change.remove(5)
                    change.append(20)
                else:
                    return False

        return True