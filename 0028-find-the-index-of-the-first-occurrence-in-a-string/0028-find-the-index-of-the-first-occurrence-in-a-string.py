class Solution:
    
    # # slicing
    # def strStr(self, haystack: str, needle: str) -> int:
    #     for i in range(len(haystack)):
    #         if haystack[i:i+len(needle)] == needle:
    #             return i
    #     return -1

    # 2 pointer
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            match = True
            for p_needle in range(len(needle)//2+(len(needle)%2)):
                if needle[p_needle] != haystack[i+p_needle] or needle[len(needle)-p_needle-1] != haystack[i+(len(needle)-p_needle-1)]:
                    match = False
                    break
            if match:
                return i
        return -1

    # # KMP [Hard]
    # def strStr(self, haystack: str, needle: str) -> int:
        