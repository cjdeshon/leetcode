class Solution:
    def decodeString(self, s: str) -> str:
        kSt = []
        sSt = [[]]
        k = 0
        
        for char in s:
            if char.isnumeric():
                k = int(char) + 10*k
            elif char == '[':
                kSt.append(k)
                sSt.append([])
                k = 0
            elif char == ']':
                sSt[-2].extend(kSt[-1]*sSt[-1])
                kSt.pop()
                sSt.pop()
            else:
                sSt[-1].append(char)
        
        return "".join(sSt[0])
                
                    
                
                
                