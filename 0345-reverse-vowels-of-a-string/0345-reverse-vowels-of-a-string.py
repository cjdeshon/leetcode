class Solution:

    def reverseVowels(self, s: str) -> str:
        # idea: use a stack to reverse the vowel order
        vowels = "aeiouAEIOU"
        vowels_stack = []
        sorted = ''
        for char in s:
            if char in vowels:
                vowels_stack.append(char)
        for char in s:
            if char in vowels:
                sorted += vowels_stack.pop()
            else:
                sorted += char
        return sorted


