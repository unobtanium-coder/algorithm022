class Solution {
public:
    bool canJump(vector<int>& nums) {
        int end = 0;
        int size = nums.size();
        for (int i = 0; (i < size) && (i <= end); ++i) {
            end = max(end, nums[i] + i);
            if (end >= (size - 1))  return true;
        }
        return false;
    }
};

