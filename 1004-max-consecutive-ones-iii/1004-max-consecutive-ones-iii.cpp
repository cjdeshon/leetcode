class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        if (k >= nums.size()) return nums.size();

        int numZeros = 0, left = 0, right = 0, maxL = 0;

        while (right < nums.size()) {
            //increment numZeros
            if (nums[right] == 0) {
                numZeros++;
            }

            //once numZeros is greater than k
            if (numZeros > k) {
                //increment left to past next zero
                if (nums[left] == 0) {
                    numZeros--;
                }
                left++;
            }

            //update max
             maxL = max(right - left + 1, maxL);

            right++;
        }

        return maxL;
    } //runtime : O(N) , space : O(1)
};