class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {

        return myApproach(nums,k);
    }

    double myApproach(vector<int>& nums, int k) {
        int n = nums.size();
        if (n < k) return -1;

        //computes sum of first window
        int max_sum = 0;
        for (int i = 0; i < k; i++) {
            max_sum += nums[i];
        }

        int current_sum = max_sum;

        //sliding window
        for(int i = k; i < n; i++) {
            current_sum += nums[i] - nums[i - k];
            max_sum = max(current_sum, max_sum);
        }

        return max_sum / (double)k;
    } //runtime : O(N) , space : O(1)
};