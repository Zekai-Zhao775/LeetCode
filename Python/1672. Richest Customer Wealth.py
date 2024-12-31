class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        wealth = []
        i = 0

        for customer in accounts:
            wealth.append(0)
            for account in customer:
                wealth[i] += account
            i += 1

        return max(wealth)