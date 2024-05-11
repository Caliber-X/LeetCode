class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        def half_adder(x: int, y: int):
            # x+y
            sum = x^y
            carry = x&y
            carry <<= 1
            if carry == 0:
                return sum
            return half_adder(sum, carry)

        def half_subtractor(x: int, y: int):
            # x-y
            diff = x^y
            borrow = (~x)&y
            borrow <<= 1
            if borrow == 0:
                return diff
            return half_subtractor(diff, borrow)
        
        if a==-b:
            return 0
        elif a==0 and b!=0:
            return b
        elif b==0 and a!=0:
            return a
        elif (a>=0 and b>=0) or (a<0 and b<0):  # same sign
            return half_adder(a, b) 
        else:
            if abs(a) < abs(b):
                a, b = b, a
            # a is bigger in scale than b
            diff = half_subtractor(abs(a), abs(b))
            if b<0: # if smaller val is -ve, total will be +ve
                return diff
            else:   # if bigger val is -ve, total will be -ve
                return -diff


        
        