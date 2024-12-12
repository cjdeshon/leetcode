class Solution:
    def reverseWords(self, s: str) -> str:
        start=end=0
        stack = []
        
        while(end < len(s)):
            #find first non-space
            start = end
            while start < len(s) and s[start] == " ":
                start += 1
                
            #break if start exceeds or matches string length
            if start >= len(s):
                break
                
            #find next space or eos
            end = start
            while end < len(s) and s[end] != " ":
                end += 1
            
            #add word to stack
            stack.append(s[start:end])
          
        #empty stack into string
        result = ""
        while stack:
            result += stack.pop()
            if stack:
                result += " "
            
        return result