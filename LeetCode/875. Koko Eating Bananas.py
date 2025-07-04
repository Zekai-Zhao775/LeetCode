from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # for each k we pick, we need O(n) to varify it's working or not
        # use binary search to pick k O(log n)

        # pick the first k, only one time, so less than O(nlog n) is ok
        # just use max as first k, cost O(n)

        # first k picking
        k = 0
        for pile in piles:
            if pile > k:
                k = pile

        # binary search
        def ifFinishEating(k):
            time = 0
            for pile in piles:
                if k >= pile:
                    time += 1
                else:
                    if pile % k == 0:
                        time += pile // k
                    else:
                        time += pile // k + 1
            # print("k = : ", k)
            # print("Eatting Time: ", time)
            if time > h:
                return False
            else:
                return True

        lower = 1
        upper = k
        last_k = k
        while lower < upper:
            k = (upper + lower) // 2
            if ifFinishEating(k):
                last_k = k
                upper = k - 1
            else:
                lower = k + 1

        if ifFinishEating(lower):
            return lower
        else:
            return last_k
