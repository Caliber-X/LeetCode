class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dict_need = {}
        for char in p:
            dict_need[char] = 1 + dict_need.get(char, 0)
        dict_window = {}
        
        l = 0
        result = []

        for r, char in enumerate(s):
            if r-l+1 > len(p):
                dict_window[s[l]] -= 1
                if dict_window[s[l]] == 0:
                    dict_window.pop(s[l])
                l += 1

            dict_window[char] = 1 + dict_window.get(char, 0)
            # print(dict_window)

            # if all(True if dict_window.get(char, 0) == dict_need[char] else False for char in dict_need):
            if dict_window == dict_need:
                result.append(l)

        return result
