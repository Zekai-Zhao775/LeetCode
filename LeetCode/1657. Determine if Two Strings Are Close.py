class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        word1Dict = {}
        word2Dict = {}

        for char in word1:
            if char not in word1Dict:
                word1Dict[char] = 1
            else:
                word1Dict[char] += 1

        for char in word2:
            if char not in word2Dict:
                word2Dict[char] = 1
            else:
                word2Dict[char] += 1

        # sort make solution O(nLogn)
        # if word1Dict.keys() == word2Dict.keys() and sorted(word1Dict.values()) == sorted(word2Dict.values()):
        #     return True
        # else:
        #     return False

        # use dict instead set here, set will cause problems if there are same values in a dict
        frequency1 = {}
        frequency2 = {}

        for value in word1Dict.values():
            if value not in frequency1:
                frequency1[value] = 1
            else:
                frequency1[value] += 1

        for value in word2Dict.values():
            if value not in frequency2:
                frequency2[value] = 1
            else:
                frequency2[value] += 1

        if word1Dict.keys() == word2Dict.keys() and frequency1 == frequency2:
            return True
        else:
            return False


