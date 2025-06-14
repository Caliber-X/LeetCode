class Solution:
    
    # slicing
    def strStr(self, haystack: str, needle: str) -> int:
        for p_haystack in range(len(haystack)):
            if haystack[p_haystack:p_haystack+len(needle)] == needle:
                return p_haystack
        return -1

    

    