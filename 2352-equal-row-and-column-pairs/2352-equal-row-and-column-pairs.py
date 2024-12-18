class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        n = len(grid)
        #get frequency of each row
        row_counter = collections.Counter(tuple(row) for row in grid)

        #add up frequency of each column present
        for c in range(n):
            col = [grid[i][c] for i in range(n)]
            count += row_counter[tuple(col)]

        return count
