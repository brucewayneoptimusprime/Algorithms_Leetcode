class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_data_structure = set()

        for i in nums:
            if i not in set_data_structure:
                set_data_structure.add(i)
            elif i in set_data_structure:
                return True
        else:
            return False
                
                
        