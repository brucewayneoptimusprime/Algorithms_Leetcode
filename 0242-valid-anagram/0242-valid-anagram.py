class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_word_dictionary = {}

        # Since a string in Python is automatically iteratable
        for each_character in s:
            if each_character not in my_word_dictionary:
                my_word_dictionary[each_character] = 1
            else:
                my_word_dictionary[each_character] += 1


        my_word_dictionary_t = {}

        for each_character in t:
            if each_character not in my_word_dictionary_t:
                my_word_dictionary_t[each_character] = 1
            else:
                my_word_dictionary_t[each_character] += 1

        if my_word_dictionary == my_word_dictionary_t:
            return True
        else:
            return False

        