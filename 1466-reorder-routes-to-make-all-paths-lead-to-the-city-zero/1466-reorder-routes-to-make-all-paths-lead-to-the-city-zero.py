class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # build 2 dicts with paths: from -> to and to -> from
        # explore paths leading to and from 0 and reverse some, count reversed paths
        # explore the connected nodes, repeat the procedure above for each node
        # while exploring check for parent to avoid recursing back
        
        
        if not connections:
            return 0
        
        paths_from = defaultdict(set)
        paths_to = defaultdict(set)
        for path in connections:
            a,b = path
            
            paths_from[a].add(b)
            paths_to[b].add(a)
            
        
        def count_paths(node,parent):
            reversed_paths = 0
            
            for i in paths_from[node]:
                if i != parent:
                    reversed_paths += 1 + count_paths(i, node)
                    
            for j in paths_to[node]:
                if j != parent:
                    reversed_paths += count_paths(j, node)
                    
            return reversed_paths
        
        return count_paths(0,0)