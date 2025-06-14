class Solution:
    
    # # slicing
    # def strStr(self, haystack: str, needle: str) -> int:
    #     for i in range(len(haystack)):
    #         if haystack[i:i+len(needle)] == needle:
    #             return i
    #     return -1

    # 2 pointer
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):

            if i+len(needle) > len(haystack) :
                return -1
            
            match = True
            for p_needle in range(len(needle)):
                if needle[p_needle] != haystack[i+p_needle]:
                    match = False
                    break
            if match:
                return i
        
        return -1


    