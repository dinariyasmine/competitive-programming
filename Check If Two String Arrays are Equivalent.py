class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word1_string = ""
        word2_string = ""
        for char in word1:
            word1_string += char
        for char in word2:
            word2_string += char
        
        if  word2_string == word1_string :
            return True
        else:
            return False
        

        