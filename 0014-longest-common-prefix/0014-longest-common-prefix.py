class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "" 

        word = strs[0]
        if len(word) == 0:
            return ""

        prefix = ""
        idx = -1
        while True:
            idx += 1
            if idx >= len(strs[0]):
                return prefix
            char = strs[0][idx]
            for word in strs:
                if idx >= len(word) or word[idx] != char:
                    return prefix
            prefix += char

        return prefix
                
