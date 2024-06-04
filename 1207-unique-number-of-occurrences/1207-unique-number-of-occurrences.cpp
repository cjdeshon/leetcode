class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        //store frequencies in unordered map
        unordered_map<int, int> freq;
        for(int num : arr) {
            freq[num]++;
        }

        //store the frequencies in unordered set
        unordered_set<int> freqSet;
        for (auto [key, value] : freq) {
            freqSet.insert(value);
        }

        //if the set size equal to map size freq are unique
        return freqSet.size() == freq.size();
        
    } //runtime : O(N), space : O(N)
};