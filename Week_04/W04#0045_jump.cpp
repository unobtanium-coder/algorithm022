class Solution {
public:
    int jump(vector<int>& nums) {
        int end = 0;
        int currend;
        int size = nums.size();
        int step = 0;
        for (int i = 0; i < size; ) {
            if (end >= size - 1)  return step;
            currend = end;
            while (i <= currend) {
                end = max(end, nums[i] + i);
                ++i;
            }
            ++step;
            // if (end >= size - 1)  return step;
        }

        return step;
    }
};
