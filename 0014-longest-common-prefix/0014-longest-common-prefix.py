class Solution:
    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     prefix = ""
    #     idx = -1
    #     while True:
    #         idx += 1
    #         if idx >= len(strs[0]):
    #             return prefix
    #         char = strs[0][idx]
    #         for word in strs:
    #             if idx >= len(word) or word[idx] != char:
    #                 return prefix
    #         prefix += char

    #     return prefix
                
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for idx, char in enumerate(strs[0]):
            for word in strs[1:]:
                if idx >= len(word) or char != word[idx]:
                    return prefix
            prefix += char
        return prefix

