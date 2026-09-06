class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap_based_dict_lol =  {}

        for current_index, current_value in enumerate(nums):
            if target - nums[current_index] not in hashmap_based_dict_lol:
                hashmap_based_dict_lol[current_value] = current_index
            elif target - nums[current_index] in hashmap_based_dict_lol:
                return [hashmap_based_dict_lol[target - nums[current_index]], current_index]

        