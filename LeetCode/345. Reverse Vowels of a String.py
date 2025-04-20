class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        for char in s:
            if char in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                vowels.append(char)

        j = 0
        result = []
        for i in range(len(s)):
            if s[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                result.append(vowels[len(vowels) - 1 - j])
                j += 1
            else:
                result.append(s[i])

        return "".join(result)