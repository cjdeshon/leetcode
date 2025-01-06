class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results = []

        def backtrack(remain, comb, next_start):
            if remain == 0 and len(comb) == k:
                #add to results
                results.append(list(comb))
                return #backtracking
            elif remain < 0 or len(comb) == k:
                #exceeded scope no need to explore further
                return

            #iterate through reduced lsit of candidates
            for i in range(next_start, 9):
                comb.append(i+1)
                backtrack(remain-i-1, comb, i+1)
                comb.pop() #backtracking for curr 

        
        backtrack(n, [], 0)

        return results