# from functools import lru_cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
                
        # Make a grid of 0's with len(text2) + 1 columns 
        # and len(text1) + 1 rows.
        dp_grid = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        
        # Iterate up each column, starting from the last one.
        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):
                # If the corresponding characters for this cell are the same...
                if text2[col] == text1[row]:
                    dp_grid[row][col] = 1 + dp_grid[row + 1][col + 1]
                # Otherwise they must be different...
                else:
                    dp_grid[row][col] = max(dp_grid[row + 1][col], dp_grid[row][col + 1])
        
        # The original problem's answer is in dp_grid[0][0]. Return it.
        return dp_grid[0][0]








        # @lru_cache(maxsize=None)
        # def memo_solve(p1,p2):
        #     #base case: either string is empty
        #     if p1==len(text1) or p2==len(text2):
        #         return 0
            
        #     #recursive case 1
        #     if text1[p1] == text2[p2]:
        #         return 1 + memo_solve(p1+1,p2+1)

        #     #recursive case 2
        #     else:
        #         return max(memo_solve(p1,p2+1), memo_solve(p1+1,p2))

        #     # #option 1: don't include text1[p1] in solution
        #     # option_1 = memo_solve(p1+1, p2)

        #     # #option 2: we include text1[p1] 
        #     # first_occurence = text2.find(text1[p1],p2)
        #     # option_2 = 0
        #     # if first_occurence != -1:
        #     #     option_2 = 1 + memo_solve(p1+1, first_occurence+1)

        #     # return max(option_1, option_2)

        # return memo_solve(0,0)