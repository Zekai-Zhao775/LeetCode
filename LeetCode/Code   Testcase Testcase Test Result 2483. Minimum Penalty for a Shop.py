class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # O(n)
        n = len(customers)
        count_Y = 0
        for c in customers:
            if c == "Y":
                count_Y += 1
        panalty = [n for i in range(n + 1)]
        panalty[0] = count_Y

        i = 1
        p_min = panalty[0]
        p_min_index = 0
        while i <= n:
            if customers[i - 1] == "Y":
                panalty[i] = panalty[i - 1] - 1
            elif customers[i - 1] == "N":
                panalty[i] = panalty[i - 1] + 1
            if panalty[i] < p_min:
                p_min = panalty[i]
                p_min_index = i
            i += 1
        return p_min_index



