class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1, p2 = 0, 0
        result = ""
        while p1 < len(word1) and p2 < len(word2):
            result += word1[p1] + word2[p2]
            p1 += 1
            p2 += 1

        if p1 < len(word1):
            result += word1[p1:]
        elif p2 < len(word2):
            result += word2[p2:]
        
        return result
        