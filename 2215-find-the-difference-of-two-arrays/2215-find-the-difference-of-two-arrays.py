class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        return [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))]

        # answer = [ [] for _ in range(2)]
        # #check 1
        # seen = set(nums2)
        # for num1 in nums1:
        #     if num1 not in seen:
        #         answer[0].append(num1)
        # #check 2
        # seen.clear()
        # seen = set(nums1)
        # for num2 in nums2:
        #     if num2 not in seen:
        #         answer[1].append(num2)

        # return answer

        