from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        def is_exit(row_dx, col_dy):
            return not (0 <= row_dx < rows and 0 <= col_dy < cols)
        
        def is_valid(row_dx, col_dy):
            return 0 <= row_dx < rows and 0 <= col_dy < cols and maze[row_dx][col_dy] == '.'
        
        
        directions = ((1,0),(0,1),(-1,0),(0,-1))
        rows = len(maze)
        cols = len(maze[0])
        queue = deque([(entrance[0],entrance[1],0)])
        seen = {(entrance[0],entrance[1])}
        
        ans = -1
        while queue:
            row, col, steps = queue.popleft()
            
            for dx, dy in directions:
                row_dx = row + dx
                col_dy = col + dy
                
                if is_exit(row_dx, col_dy) and (row,col) != (entrance[0], entrance[1]):
                    ans = steps
                    queue = deque()
                    break
                
                if is_valid(row_dx, col_dy) and (row_dx, col_dy) not in seen:
                    seen.add((row_dx, col_dy))
                    queue.append((row_dx, col_dy, steps + 1))
                
        
        return ans