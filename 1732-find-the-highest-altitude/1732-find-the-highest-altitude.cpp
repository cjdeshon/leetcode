class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int maxA = 0, curA = 0;
        
        for (int i = 0; i < gain.size(); i++) {
            curA = curA + gain[i];
            maxA = max(maxA, curA);
        }
        
        return maxA;
    }
};