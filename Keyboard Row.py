class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        output = []
        first_row = set("qwertyuiop")
        second_row = set("asdfghjkl")
        third_row = set ("zxcvbnm")
        
        for word in words:
            word_set = set(word.lower())
            if word_set <= first_row or word_set <= second_row or word_set <= third_row:
                output.append(word)
            

        return output
        
