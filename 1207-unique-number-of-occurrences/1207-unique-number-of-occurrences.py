class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return len(set(Counter(arr).values())) == len(set(arr))
        
        
        
        
#         unordered_map = {}
#         for num in arr:
#             if num in unordered_map:
#                 unordered_map[num] = unordered_map[num] + 1
#             else:
#                 unordered_map[num] = 1
                
#         return len(unordered_map.keys()) == len(set(unordered_map.values()))
        