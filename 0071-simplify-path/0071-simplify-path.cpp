class Solution {
public:
    string simplifyPath(string path) {
        stack<string> stringStack;
        stringstream ss(path);
        string currentString;
        
        while(getline(ss, currentString, '/')) {
            //if current compenent is "..", then pop
            if(currentString == "..") {
                if(!stringStack.empty()) stringStack.pop();
            } else if (currentString != "." && !currentString.empty()) {
                //add legit dir
                stringStack.push(currentString);
            }
        }

        //construct path
        string answer = "";
        while (!stringStack.empty()) {
            answer = "/" + stringStack.top() + answer;
            stringStack.pop();
        }
        if (answer.empty()) return "/";
        else return answer;
    }
};