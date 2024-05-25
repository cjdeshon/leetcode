class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int leftSum = 0, totalSum = 0;

        //total sum
        for (int i = 0; i < nums.size(); i++) {
            totalSum += nums[i];
        }

        cout << totalSum << endl;
        //check pivot
        if (totalSum - nums[0] == 0) return 0;
        for (int i = 1; i < nums.size(); i++) {
            leftSum += nums[i - 1];
            cout << leftSum << " and " << totalSum - leftSum - nums[i] << endl;
            if (leftSum == totalSum - leftSum - nums[i]) return i;
        }


        return -1;
    }
}; //runtime : O(N), space : O(1)