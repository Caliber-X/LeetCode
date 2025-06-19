class Solution:

    # # bad, fails in big data cases
    # def minWindow(self, s: str, t: str) -> str:
    #     l, r = 0, len(t)-1
    #     count_have = 0
    #     dict_have = {}
    #     count_need = len(t)
    #     dict_need = {}
    #     for char in t:
    #         if char not in dict_need.keys():
    #             dict_need[char] = 0
    #             dict_have[char] = 0
    #         dict_need[char] += 1
        
    #     for i in range(l, r+1):
    #         if i < len(s) and s[i] in dict_have.keys():
    #             dict_have[s[i]] += 1
    #             count_have += 1
    #     substr = [l, r]

    #     # print(f"{count_have=}")
    #     # print(f"{dict_have=}")
    #     # print(f"{count_need=}")
    #     # print(f"{dict_need=}")
    #     # return ""

    #     res = [-1, -1]
    #     reslen = None

    #     while r < len(s):
    #         # print(f"{l=} {r=} {count_have=} {dict_have=}")
    #         r_incremented = False

    #         if s[r] not in dict_need.keys():
    #             r_incremented = True

    #         elif count_have >= count_need:
    #             if all(True if dict_have[char]-dict_need[char]>=0 else False for char in t):
    #                 if reslen is None or substr[1]-substr[0]+1 < reslen:
    #                     res = substr.copy()
    #                     reslen = substr[1]-substr[0]+1
    #                     # print(f"{res=}")
    #                 if l < len(s) and s[l] in dict_have:
    #                     dict_have[s[l]] -= 1
    #                     count_have -= 1
    #                 l += 1
    #                 substr[0] += 1
    #                 if r-l < len(t)-1:
    #                     r_incremented = True
    #             else:
    #                 r_incremented = True

    #         elif count_have < count_need:
    #             r_incremented = True

    #         if r_incremented:
    #             r += 1
    #             if r < len(s):
    #                 if s[r] in dict_have:
    #                     dict_have[s[r]] += 1
    #                     count_have += 1
    #                 substr[1] += 1

    #     return s[res[0]:res[1]+1] if reslen is not None else ""

    def minWindow(self, s: str, t: str) -> str:
        # have
        count_have = 0
        dict_have = {}
        # need
        dict_need = {}
        for char in t:
            dict_need[char] = dict_need.get(char, 0) + 1
        count_need = len(dict_need)
        
        l = 0
        res = [-1, -1]
        reslen = None

        for r in range(len(s)):

            dict_have[s[r]] = dict_have.get(s[r], 0) + 1

            if s[r] in dict_need and dict_have[s[r]] == dict_need[s[r]]:
                count_have += 1

            while count_have == count_need:
                
                windowlen = r-l+1
                if reslen is None or windowlen < reslen:
                    res = [l, r]
                    reslen = windowlen

                dict_have[s[l]] -= 1
                if s[l] in dict_need and dict_have[s[l]] < dict_need[s[l]]:
                    count_have -= 1
                l += 1
        
        return s[res[0]:res[1]+1] if reslen is not None else ""
        

