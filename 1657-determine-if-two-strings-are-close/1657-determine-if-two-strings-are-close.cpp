class Solution {
public:
    bool closeStrings(string word1, string word2) {
        //check that word1 and word2 are same size
        if(word1.size() != word2.size()) return false;

        return checkFreq(word1, word2);
    }

    bool checkFreq(string word1, string word2) {
        //check occurance of each char in word1
        unordered_map<char, int> word1Map;
        for(char c : word1) {
            word1Map[c] = word1Map[c] + 1;
        }
        //check occurance of each char in word2
        unordered_map<char, int> word2Map;
        for(char c : word2) {
            word2Map[c] = word2Map[c] + 1;
        }
        //store chars and frequency values in vectors to check words can be manipulated
        vector<char> word1KeySet, word2KeySet, word1Freq, word2Freq;
        for (auto keyValuePair : word1Map) {
            word1KeySet.push_back(keyValuePair.first);
            word1Freq.push_back(keyValuePair.second);
        }
        for(auto keyValuePair : word2Map) {
            word2KeySet.push_back(keyValuePair.first);
            word2Freq.push_back(keyValuePair.second);
        }

        //check that chars are the same
        sort(word1KeySet.begin(), word1KeySet.end());
        sort(word2KeySet.begin(), word2KeySet.end());
        if(word1KeySet != word2KeySet) return false;

        //check that freq are the same
        sort(word1Freq.begin(), word1Freq.end());
        sort(word2Freq.begin(), word2Freq.end());
        return word1Freq == word2Freq;
    } //runtime : O(N), space : O(N)

    

    
};