class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = ""

        for ch in s:
            if ch.isalnum():
                palindrome += ch.lower()
        
        return palindrome == palindrome[::-1]
        