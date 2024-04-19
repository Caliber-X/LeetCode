class Solution:
    def __init__(self):
        self.precedence = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
    def romanToInt(self, s: str) -> int:
        sum = 0
        for i in range(len(s)):
            x = self.precedence[s[i]]
            if i<len(s)-1 and self.precedence[s[i]] < self.precedence[s[i+1]]:
                x *= -1
            sum += x
        return sum
