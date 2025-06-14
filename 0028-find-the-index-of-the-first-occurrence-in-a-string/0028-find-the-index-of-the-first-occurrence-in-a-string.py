class Solution:
    
    # # slicing
    # def strStr(self, haystack: str, needle: str) -> int:
    #     for i in range(len(haystack)):
    #         if haystack[i:i+len(needle)] == needle:
    #             return i
    #     return -1

    # 2 pointer
    def strStr(self, haystack: str, needle: str) -> int:
        H, N = len(haystack), len(needle)
        for i in range(H-N+1):
            match = True
            for p_needle in range((N//2)+(N%2)):
                if needle[p_needle] != haystack[i+p_needle] or needle[N-p_needle-1] != haystack[i+(N-p_needle-1)]:
                    match = False
                    break
            if match:
                return i
        return -1

    # # KMP [Hard]
    # def strStr(self, haystack: str, needle: str) -> int:
        