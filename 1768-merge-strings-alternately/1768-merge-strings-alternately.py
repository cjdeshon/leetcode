class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        point1=point2=0
        ans = ""
        while point1 < len(word1) or point2 < len(word2):
            if point1 < len(word1):
                ans += word1[point1]
                point1 += 1
            
            if point2 < len(word2):
                ans += word2[point2]
                point2 += 1

            # print(ans)

        return ans

    