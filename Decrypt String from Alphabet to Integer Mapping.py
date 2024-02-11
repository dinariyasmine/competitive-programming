class Solution:
    def freqAlphabets(self, s: str) -> str:
        formed = ""
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == "#":
                value = int(s[i:i + 2]) + 96
                i += 3  
            else:
                value = int(s[i]) + 96
                i += 1
            formed += chr(value)
        return formed
