from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        
        #step 1 build the initial set of rotton oranges
        fresh_oranges = 0
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue. append((r,c))
                    
                elif grid[r][c]== 1:
                    fresh_oranges += 1
                    
        #mark the round/level
        queue.append((-1,-1))
        
        #step 2 start the rotting process w BFS
        minutes_elapsed = -1
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while queue:
            row, col = queue.popleft()
            if row == -1:
                #finished one round of processing
                minutes_elapsed += 1
                if queue: #avoidng endless
                    queue.append((-1,-1))
            
            else:
                #start contamination
                for d in dirs:
                    neighbor_row, neighbor_col = row + d[0], col + d[1]
                    if rows > neighbor_row >= 0 and cols > neighbor_col >= 0:
                        if grid[neighbor_row][neighbor_col] == 1:
                            #contaminate
                            grid[neighbor_row][neighbor_col] = 2
                            fresh_oranges -= 1
                            queue.append((neighbor_row, neighbor_col))
                            
        return minutes_elapsed if fresh_oranges == 0 else -1