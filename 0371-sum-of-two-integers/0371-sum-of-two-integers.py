class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        # half adder (add 2 binary bits)
        def half_adder(x: int, y: int):
            # x & y must be single bit
            sum = x^y
            carry = x&y
            return 2*carry+sum
        
        return half_adder(a,b)
        
        