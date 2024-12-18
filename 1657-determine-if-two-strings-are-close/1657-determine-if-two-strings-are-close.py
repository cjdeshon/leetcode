class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1,c2 = Counter(word1), Counter(word2)
        
        return sorted(c1.values()) == sorted(c2.values()) and sorted(c1.keys()) == sorted(c2.keys())
        
        
        
#         word1Dict = {}
#         for char in word1:
#             if char not in word1Dict:
#                 word1Dict[char] = 1
#             else:
#                 word1Dict[char] += 1
                
#         word2Dict = {}
#         for char in word2:
#             if char not in word2Dict:
#                 word2Dict[char] = 1
#             else:
#                 word2Dict[char] += 1
                
#         return sorted(word1Dict.values()) == sorted(word2Dict.values()) and (sorted(word1Dict.keys()) == sorted(word2Dict.keys()))