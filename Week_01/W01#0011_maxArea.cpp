class Solution {
public:
    int maxArea(vector<int>& height) {
        int i, j;
        int hi, hj;
        int s;

        i = 0;
        hi = height[i];
        j = height.size() - 1;
        hj = height[j];

        s = 0;

        while (i < j)
        {
            s = max(s, (j-i)*min(hi, hj));

            if (hi <= hj)
            {
                ++i;
                hi = height[i];
            }
            else
            {
                --j;
                hj = height[j];
            }
        }

        return s;
    }
};

