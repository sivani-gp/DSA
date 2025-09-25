class Solution:
    def isPalindrome(self, x: int) -> bool:
        x1=str(x)
        if x1[::-1]==x1:
            return True
        return False

        