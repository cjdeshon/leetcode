class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum = -1
        curArea = 0
        pointL, pointR = 0, len(height)-1
        
        while(pointR > pointL):
            curArea = min(height[pointL],height[pointR]) * (pointR-pointL)
            print(curArea)
            maximum = max(maximum, curArea)
            
            if height[pointL] < height[pointR]:
                pointL += 1
            else:
                pointR -= 1
                
        return maximum