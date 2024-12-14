class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        LengthS, LengthT = len(s), len(t)

        s_pointer = t_pointer = 0
        while s_pointer < LengthS and t_pointer < LengthT:
            #check for match
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
            t_pointer += 1

        return s_pointer == LengthS

        # RECURSIVE SOLUTION
        # def rec_isSubsequence(s_index, t_index):
        #     # base cases
        #     if s_index == LengthS:
        #         return True
        #     if t_index == LengthT:
        #         return False
        #     # consume both string or target string
        #     if s[s_index] == t[t_index]:
        #         s_index += 1
        #     t_index += 1

        #     return rec_isSubsequence(s_index, t_index)

        # return rec_isSubsequence(0,0)
            