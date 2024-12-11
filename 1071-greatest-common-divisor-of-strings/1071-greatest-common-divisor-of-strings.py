class Solution:
    def isValid(self, len_base:int, str1:str, base:str): 
        numConcat = len(str1) // len_base

        return str1 == numConcat * base

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len_base = min(len(str1), len(str2))

        while len_base > 0:
            if len(str1) % len_base == 0 and len(str2) % len_base == 0:
                base = str1[:len_base]
                str1_valid = self.isValid(len_base, str1, base)
                str2_valid = self.isValid(len_base, str2, base)

                if str2_valid and str1_valid:
                    return str1[:len_base]
            
            str1_valid = False
            str2_valid = False
            len_base -= 1
    
        return ""
        

