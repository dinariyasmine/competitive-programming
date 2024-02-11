class Solution:
    def defangIPaddr(self, address: str) -> str:
        modified_adress=""
        for char in address:
            if char == ".":
                
                modified_adress += "[.]"
            else:
                modified_adress += char

        return modified_adress
        