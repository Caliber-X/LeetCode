class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        window = set()
        max_len = 0
        while r < len(s):
            if s[r] in window:
                max_len = max(max_len, len(window))
                while True:
                    window.remove(s[l])
                    l += 1
                    if s[l-1] == s[r]:
                        break
            window.add(s[r])
            # print(window)
            r += 1

        return max(max_len, len(window))


