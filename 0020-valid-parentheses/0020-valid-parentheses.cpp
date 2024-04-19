class Solution {
public:
    bool isValid(string s) {
        int a=0, b=0, c=0;
        std::vector <char>stack;
        for (int i=0; i<s.size(); i++) {
            if (s[i] == '(')        stack.push_back(s[i]);
            else if (s[i] == ')') {
                if (stack.size()==0 || stack.back() != '(')
                    return false;
                else
                    stack.pop_back();
            }
            if (s[i] == '[')        stack.push_back(s[i]);
            else if (s[i] == ']') {
                if (stack.size()==0 || stack.back() != '[')
                    return false;
                else
                    stack.pop_back();
            }
            if (s[i] == '{')        stack.push_back(s[i]);
            else if (s[i] == '}') {
                if (stack.size()==0 || stack.back() != '{')
                    return false;
                else
                    stack.pop_back();
            }
        }
        if (stack.size()==0)
            return true;
        return false;
    }
};