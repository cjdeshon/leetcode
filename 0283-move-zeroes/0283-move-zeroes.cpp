class Solution {
public:
    void moveZeroes(vector<int>& nums) {
       if (nums.size() > 1)
        // return myApproach(nums);
        return optimal(nums);


    }

    /*
    pointer to current and index and pointer to next nonzero
    */
    void myApproach(vector<int>& nums) {

        int start = 0;
        int end = nums.size();
        int pointer = start;

        while (start < end) {
            //find index first zero
            while (nums[start] != 0) {
                start++;
                if (start == end) return;
            }
            //find index of next nonzero
            pointer = start;
            while(nums[pointer] == 0) {
                pointer++;
                if (pointer == end) break;
            }
            //replace first zero
            if (pointer < end) {
                nums[start] = nums[pointer];
                nums[pointer] = 0;
                start++;
            }
            else break;
        }
    } //runtime : O(N) , Space O(1)

    void optimal(vector<int>& nums) {
        for (int lastNonZero = 0, cur = 0; cur < nums.size(); cur++) {
            if (nums[cur] != 0) {
                swap(nums[lastNonZero++], nums[cur]);
            }
        }
    } //runtime : O(N) , space : O(1)
};