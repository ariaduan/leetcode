class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <0: return False
        tmp = str(x)
        tmpr = tmp[::-1]
        if tmp==tmpr: return True
        return False
