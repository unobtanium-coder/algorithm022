class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def backtrack(current_len = 0):
            if current_len == n:  
                res.append(nums[:])
                return
            backtrack(current_len + 1)
            for i in range(0, current_len):
                nums[current_len], nums[i] = nums[i], nums[current_len]
                backtrack(current_len + 1)
                nums[current_len], nums[i] = nums[i], nums[current_len]
        
        nums.sort()
        n = len(nums)
        res = []
        backtrack()
        return res

