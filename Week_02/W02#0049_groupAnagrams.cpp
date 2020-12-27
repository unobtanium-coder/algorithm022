class Solution {
public:
    vector<vector<string> > groupAnagrams(vector<string>& strs)
    {
        vector<pair<string, int> > str2;
        vector<vector<string> > ans;
        vector<string> temp;
        string tmp;
        int n = strs.size();
        int l, r;
        int i, j;

        for (i = 0; i < n; ++i)
        {
            tmp = strs[i];
            sort(tmp.begin(), tmp.end());
            str2.emplace_back(make_pair(tmp, i));
        }
        sort(str2.begin(), str2.end());
        
        l = 0; r = 0;
        for (i = 0; r < n; ++i)
        {
            while (r < n && str2[l].first == str2[r].first)
                ++r;
            for (j = l; j < r; ++j)
                temp.emplace_back(strs[str2[j].second]);
            ans.emplace_back(temp);
            temp.clear();
            l = r;
        }

        return ans;
    }
};

