class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse_string = str(x)[::-1]
        return str(x) == reverse_string