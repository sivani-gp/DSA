class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        sign = -1 if x<0 else 1
        x=abs(x)
        num = 0
        while x != 0:
            digit = x%10
            num = (num*10) + digit
            x=x//10

            #check for overflow
            if num>INT_MAX or num<INT_MIN:
                return 0
            
        return num*sign
        