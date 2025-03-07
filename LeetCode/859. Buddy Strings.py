class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        i = 0
        count = 0

        if len(s) != len(goal):
            return False

        list_s_diff = []
        list_goal_diff = []

        while i < len(s):
            if s[i] != goal[i]:
                list_s_diff.append(s[i])
                list_goal_diff.append(goal[i])
                count += 1

            i += 1
        if count == 2:
            if list_s_diff[0] == list_goal_diff[1] and list_s_diff[1] == list_goal_diff[0]:
                return True

                # "aa" "aa" like
        if count == 0:
            for char in s:
                if s.count(char) > 1:
                    return True

        return False

