class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        stack<int> st;

        for(int asteroid : asteroids) {
            int flag = 1;
            
            //check possible collisions
            while(!st.empty() && (st.top() > 0 && asteroid < 0)) {
                //top asteroid is smaller
                if (abs(st.top()) < abs(asteroid)) {
                    st.pop();
                    continue;
                }
                //asteroids are same size
                else if (abs(st.top()) == abs(asteroid)) {
                    st.pop();
                }
                //current asteroid is samller
                flag = 0;
                break;
            }

            if (flag) {
                st.push(asteroid);
            }
        }

        //add asteroids from stack to vector in reverse order
        vector<int> remaining (st.size());
        for(int i = remaining.size() - 1; i >= 0; i--) {
            remaining[i] = st.top();
            st.pop();
        }

        return remaining;
    } //runtime : O(N), space : O(N)
};