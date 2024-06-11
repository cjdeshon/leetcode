class Solution {
public:
    string decodeString(string s) {
        // return charStack(s);
        return doubleStack(s);
    }

    string charStack(string s) {
        stack<char> stack;
        for(int i = 0; i < s.length(); i++) {
            if(s[i] == ']') {
                string decodedString = "";
                //get encoded string
                while (stack.top() != '[') {
                    decodedString += stack.top();
                    stack.pop();
                }
                //pop [ from stack]
                stack.pop();

                int base = 1;
                int k = 0;
                //get k
                while(!stack.empty() && isdigit(stack.top())) {
                    k = k + (stack.top() - '0') * base;
                    stack.pop();
                    base *= 10;
                }

                int currentLen = decodedString.size();
                //decode k[decodedString], by pushing decodedString k times into stack
                while(k != 0) {
                    for (int j = decodedString.size() - 1; j >= 0; j--) {
                        stack.push(decodedString[j]);
                    }
                    k--;
                }
            }

            //push current character to stack
            else {
                stack.push(s[i]);
            }
        }

        //get result from stack
        string result;
        for(int i = stack.size() - 1; i >=0; i--) {
            result = stack.top() + result;
            stack.pop();
        }

        return result;
    } //runtime : O(maxK^(countK)* N), space : O(sum(maxK^(countK) * n))

    string doubleStack(string s) {
        stack<int> countStack;
        stack<string> stringStack;
        string currentString;
        int k = 0;
        for(auto ch : s) {
            if (isdigit(ch)) {
                k = k * 10 + ch - '0';
            } 
            else if (ch == '[') {
                //push the number k to countStack
                countStack.push(k);
                // push the currentString to stringStack
                stringStack.push(currentString);
                //reset currentString and k
                currentString = "";
                k = 0;
            }
            else if (ch == ']') {
                string decodedString = stringStack.top();
                stringStack.pop();
                //decode currentK[currentString] by appending currentString k times
                for (int currentK = countStack.top(); currentK > 0; currentK--) {
                    decodedString += currentString;
                }
                countStack.pop();
                currentString = decodedString;
            }
            else {
                currentString += ch;
            }
        }

        return currentString;
    }
};