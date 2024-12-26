class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        num_cities = len(isConnected)
        num_provinces = 0
        is_visited = set()
        
        def dfs(curr):
            is_visited.add(curr)
            for i in range(num_cities):
                if (isConnected[curr][i] == 1 and i not in is_visited):
                    dfs(i)

        for i in range(num_cities):
            if i not in is_visited:
                num_provinces += 1
                dfs(i)
        
        return num_provinces