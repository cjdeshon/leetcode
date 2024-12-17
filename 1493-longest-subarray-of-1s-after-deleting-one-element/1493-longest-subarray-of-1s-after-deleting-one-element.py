class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start, maxWindow, lastZero = 0,0,-1
        n = len(nums)

        for i in range(n):
            if nums[i] == 0:
                start = lastZero + 1
                lastZero = i
            maxWindow = max(maxWindow, i - start)

        return maxWindow
                
            