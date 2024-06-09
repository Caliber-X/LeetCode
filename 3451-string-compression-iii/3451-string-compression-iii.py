class Solution:

    def compressedString(self, word: str) -> str:
        
        if len(word) == 0:
            return ""

        if len(word) == 1:
            return "1"+word
        
        def write_char_count(count: int, char_: str):
            q, r = divmod(count, 9)
            comp = q*f"9{char_}" 
            if r!=0:
                comp += f"{r}{char_}"
            return comp

        comp = ""
        count = 1

        for i in range(len(word)-1):
            current_char, next_char = word[i], word[i+1]

            if current_char != next_char:
                comp += write_char_count(count, current_char)
                count = 1
            
            else:
                count += 1

            if i == len(word)-2:
                comp += write_char_count(count, next_char)

        return comp
