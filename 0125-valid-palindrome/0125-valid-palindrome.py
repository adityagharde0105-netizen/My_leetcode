class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = ""

        for ch in s:
            if ch.isalnum():
                palindrome += ch.lower()
        
        return palindrome == palindrome[::-1]


'''left = 0
        right = len(s)-1

        while left > right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True'''



        