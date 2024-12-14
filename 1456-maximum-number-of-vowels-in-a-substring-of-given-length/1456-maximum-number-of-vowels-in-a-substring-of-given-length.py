class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}  # Set of vowels
        maxVowel = 0
        curVowel = 0
        
        # Initialize the first window
        for i in range(k):
            if s[i] in vowels:
                curVowel += 1
        maxVowel = curVowel
        
        # Slide the window across the string
        for i in range(k, len(s)):
            # Add the new character to the window
            if s[i] in vowels:
                curVowel += 1
            # Remove the character that's sliding out of the window
            if s[i - k] in vowels:
                curVowel -= 1
            
            # Update the maximum vowel count
            maxVowel = max(maxVowel, curVowel)
        
        return maxVowel
            