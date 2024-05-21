class Solution {
public:
    int maxVowels(string s, int k) {
        return myApproach(s,k);
    }

    bool isVowel(char c) {
        static const unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u'};
        return vowels.find(c) != vowels.end();
    }
    int myApproach(string s, int k) {
        int n = s.length();
        if (n < k) return -1;

        //first pass through window
        int max_vowel = 0;
        for (int i = 0; i < k; i++) {
            if(isVowel(s[i])) max_vowel++;
        }
        int current_vowel = max_vowel;

        //sliding window
        for (int i = k; i < n; i++) {
            if(isVowel(s[i])) current_vowel++;
            if(isVowel(s[i - k])) current_vowel--;
            max_vowel = max(current_vowel, max_vowel);
        }

        return max_vowel;
    }
};