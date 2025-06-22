class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dict_need = {}
        for char in p:
            dict_need[char] = 1 + dict_need.get(char, 0)
        count_need = sum(dict_need.values())
        dict_window = {}
        count_have = 0
        
        l = 0
        result = []

        for r, char in enumerate(s):
            dict_window[char] = 1 + dict_window.get(char, 0)
            count_have += 1
            
            if count_have == count_need:
                if all(True if dict_window.get(char, 0) == dict_need[char] else False for char in dict_need):
                    result.append(l)
                dict_window[s[l]] -= 1
                l += 1
                count_have -= 1

        return result
