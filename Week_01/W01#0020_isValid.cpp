class Solution {
public:
    bool isValid(string s) {
        stack<char> stck;
        int n = s.size();

        for (int i = 0; i < n; ++i)
        {
            if (s[i] == '(' || s[i] == '[' || s[i] == '{')
                stck.push(s[i]);
            else if (stck.empty())
                return false;
            else if (s[i] == ')' && stck.top() == '(')
                stck.pop();
            else if (s[i] == ']' && stck.top() == '[')
                stck.pop();
            else if (s[i] == '}' && stck.top() == '{')
                stck.pop();
            else
                return false;
        }

        return stck.empty();
    }
};

