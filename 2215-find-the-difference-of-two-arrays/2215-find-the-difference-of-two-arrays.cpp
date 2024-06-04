class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        // return BruteForce(nums1,nums2);
        return {hashSet(nums1, nums2), hashSet(nums2, nums1)};
    }
    
    //approach 1
    vector<vector<int>> BruteForce(vector<int>& nums1, vector<int>& nums2) {
        vector<vector<int>> uniqueNums;
        
        //check for nums1 in nums2
        vector<int>onlyNums1;
        bool found = false;
        for(int i = 0; i < nums1.size(); i++) {
            found = false;
            
            for(int j = 0; j < nums2.size(); j++) {
                if (nums1[i] == nums2[j]) found = true;
            }
            
            if (found == false) {
                onlyNums1.push_back(nums1[i]);
            }
        }
        
        //check for nums2 in nums1
        vector<int>onlyNums2;
        for(int i = 0; i < nums2.size(); i++) {
            found = false;
            
            for(int j = 0; j < nums1.size(); j++) {
                if (nums1[j] == nums2[i]) found = true;
            }
            
            if (found == false) {
                onlyNums2.push_back(nums2[i]);
            }
        }
        
        //sort vectors and remove duplicates
        sort(onlyNums1.begin(), onlyNums1.end());
        auto it = unique(onlyNums1.begin(), onlyNums1.end());
        onlyNums1.resize(distance(onlyNums1.begin(), it));

        sort(onlyNums2.begin(), onlyNums2.end());
        it = unique(onlyNums2.begin(), onlyNums2.end());
        onlyNums2.resize(distance(onlyNums2.begin(), it));

        //add both vectors and return answer
        uniqueNums.push_back(onlyNums1);
        uniqueNums.push_back(onlyNums2);
        return uniqueNums;
        
    } //runtime : O(n*m) + O(nlgn) + O(mlgm) , space : O(n + m)

    //approach 2
    vector<int> hashSet(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> onlyInNums1;

        //store nums2 elements in unordered set
        unordered_set<int> existsInNums2;
        for(int num: nums2) {
            existsInNums2.insert(num);
        }

        //iterate over each element in the list nums1
        for (int num : nums1) {
            if (existsInNums2.find(num) == existsInNums2.end()) {
                onlyInNums1.insert(num);
            }
        }

        //convert to vector
        return vector<int> (onlyInNums1.begin(), onlyInNums1.end());
    } //runtime : O(N + M), space : O(max(N,M))
    
};