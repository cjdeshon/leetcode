class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        window = sum(nums[:k])
        maxSum = window

        for i in range (k, n):
            window += nums[i] - nums[i-k]
            maxSum = max(window, maxSum)

        return maxSum / k