from ast import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        comm = ""
        for i in range(len(strs[0])):
            for string in strs[1:]:
                if i >= len(string) or string[i] != strs[0][i]:
                    return comm
            comm += strs[0][i]
        return comm