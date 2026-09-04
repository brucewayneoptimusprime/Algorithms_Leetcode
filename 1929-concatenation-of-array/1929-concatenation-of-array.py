class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        
        length_of_initial_array = len(nums)
        ans = [None] * (length_of_initial_array * 2)

        for i in range(0, len(nums)):
            ans[i] = nums[i]
            ans[i + length_of_initial_array] = nums[i]

        return ans
        