class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # p1, p2 = 0, 0   # t, s
        
        # if p1 == len(t) and p2 == len(s):   # both empty
        #     return True
        # if p1 == len(t):
        #     return False

        # while p2 < len(s):
        #     if t[p1] == s[p2]:
        #         p1 += 1
        #         p2 += 1
        #     else:
        #         p1 += 1
        #     if p1 == len(t) and p2 < len(s):
        #         return False
        
        # return True

        idx = 0
        for _t in t:
            if idx < len(s) and _t == s[idx]:
                idx += 1
                if idx == len(s):
                    break
        return idx == len(s)

