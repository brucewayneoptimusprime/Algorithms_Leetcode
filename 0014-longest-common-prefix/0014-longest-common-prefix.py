class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        sorted_array_according_to_length = sorted(strs, key = len)
        saatl = sorted_array_according_to_length

        prefix_list = []
        
        for i in range(0, len(saatl[0])):
            reference_character = saatl[0][i]

            for x in range(len(saatl)):
                if saatl[x][i] != reference_character:
                    return "".join(prefix_list)
            
            prefix_list.append(reference_character)

        return "".join(prefix_list)
            



        