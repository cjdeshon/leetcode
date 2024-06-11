class Solution {
public:
    int equalPairs(vector<vector<int>>& grid) {
        // return brute(grid);
        return rowFreq(grid);
    }

    int brute(vector<vector<int>>& grid) {
        int count = 0;
        int n = grid.size();

        //check each row r against each column c
        for(int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {
                bool match = true;

                //iterate over row r and column c
                for (int i = 0; i < n; i++) {
                    if (grid[r][i] != grid[i][c]) {
                        match = false;
                        break;
                    }
                }

                //if row r equals column c, increment count by 1
                count += match ? 1 : 0;
            }
        }


        return count;
    } //runtime : O(N^3), space : O(1)

    string vectorToString(const vector<int>& vec) {
        ostringstream oss;
        for (int i = 0; i < vec.size(); i++) {
            if (i != 0) {
                oss << ",";
            }
            oss << vec[i];
        }

        return oss.str();
    }
    int rowFreq(vector<vector<int>>& grid) {
        int count = 0;
        int n = grid.size();

        //keep track of frequency of each row
        unordered_map<string,int> rowCounter;
        for(const auto& row : grid) {
            string rowString = vectorToString(row);
            rowCounter[rowString]++;
        }

        //add up frequency of each column in map
        for (int c = 0; c < n; c++) {
            vector<int> colArray(n);
            for(int r = 0; r < n; r++) {
                colArray[r] = grid[r][c];
            }

            string colString = vectorToString(colArray);
            count += rowCounter[colString];
        }

        return count;
    }
};