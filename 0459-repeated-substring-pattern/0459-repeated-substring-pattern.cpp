class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        return checksubstr(s);
        // return rotate(s);
    }

    bool checksubstr(string s) {
        int n = s.length();

        for(int i = 1; i <= n/2; i++) {
            //check if substr is  possible
            if (n % i == 0) {
                string pattern = "";
                for(int j = 0; j < n / i; j++) {
                    pattern += s.substr(0,i);
                }
                if (s==pattern) return true;
            }
        }

        return false;
    } //runtime : O(n * rt(n)), space : O(N)

    bool rotate(string s) {
        string t = s + s;
        if (t.substr(1, t.size() - 2).find(s) != -1) return true;
        return false;
    }
};