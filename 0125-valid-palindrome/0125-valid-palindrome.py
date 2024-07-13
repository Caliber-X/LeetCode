class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s)-1
        while start < end:
            
            val_start = s[start]
            if not val_start.isalnum():
                start += 1
                continue
            
            val_end = s[end]
            if not val_end.isalnum():
                end -= 1
                continue
            
            val_start, val_end = val_start.lower(), val_end.lower()

            if val_start != val_end:
                return False
            
            start += 1
            end -= 1
        
        return True
