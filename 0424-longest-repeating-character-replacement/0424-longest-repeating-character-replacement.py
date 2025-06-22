class Solution:
    # # O(26.n)
    # def characterReplacement(self, s: str, k: int) -> int:
    #     window = {}
    #     l = 0
    #     max_len = 0
    #     for r in range(len(s)):
    #         window[s[r]] = 1 + window.get(s[r], 0)
    #         while (r-l+1) - max(window.values()) > k:
    #             window[s[l]] -= 1
    #             l += 1
    #         max_len = max(max_len, r-l+1)
    #     return max_len

    # # O(n)
    # def characterReplacement(self, s: str, k: int) -> int:
    #     window = {}
    #     l = 0
    #     max_len = 0
    #     maxf = 0 
    #     for r in range(len(s)):
    #         window[s[r]] = 1 + window.get(s[r], 0)
    #         maxf = max(maxf, window[s[r]])
    #         while (r-l+1) - maxf > k:
    #             window[s[l]] -= 1
    #             l += 1
    #         max_len = max(max_len, r-l+1)
    #     return max_len
        
    # O(26.n), better space complexity using array
    def characterReplacement(self, s: str, k: int) -> int:
        window = [0] * 26
        l = 0
        max_len = 0
        for r in range(len(s)):
            window[ord(s[r]) - 65] += 1
            while (r-l+1) - max(window) > k:
                window[ord(s[l]) - 65] -= 1
                l += 1
            max_len = max(max_len, r-l+1)
        return max_len