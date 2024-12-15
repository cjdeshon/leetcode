class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        for right in range(len(nums)):
            print(k, nums[right])
            k -= (1 - nums[right])
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
        return right - left + 1
            
