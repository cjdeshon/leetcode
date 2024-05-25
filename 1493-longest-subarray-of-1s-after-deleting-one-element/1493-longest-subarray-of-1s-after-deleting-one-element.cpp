class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int right = 0, left = 0, deleted = 0, maxL = 0;

        while (right < nums.size()) {
            if (nums[right] == 0) deleted++;

            if (deleted > 1) {
                if (nums[left] == 0) deleted--;
                left++;
            }

            maxL = max(maxL, right - left);

            right++;
        }

        return maxL;
    } //runtime : O(N) , space : O(1)
};