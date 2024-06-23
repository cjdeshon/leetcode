class Solution {
public:
    string predictPartyVictory(string senate) {
        //create two queues to keep track of eligible senators separately in sorted order
        int n = senate.size();
        queue<int> rQueue;
        queue<int>dQueue;

        //populate queues with indicies of respective senators from left to right
        for (int i = 0; i < n; i++) {
            if (senate[i] == 'R') {
                rQueue.push(i);
            } else {
                dQueue.push(i);
            }
        }

        //while both Queues have at least one senator
        while (!rQueue.empty() && !dQueue.empty()) {
            //pop Next-Turn Sentate from both Queues
            int rTurn = rQueue.front();
            rQueue.pop();
            int dTurn = dQueue.front();
            dQueue.pop();

            //larger index is banned. Smaller index en-Queue + N for next round turn
            if (dTurn < rTurn) {
                dQueue.push(dTurn + n);
            } else {
                rQueue.push(rTurn + n);
            }
        }

        //return non empty
        return rQueue.empty() ? "Dire" : "Radiant";
    } //runtime : O(N), space : O(N)
};