class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}

        left = 0 
        max_lenght = 0


        for right in range(len(s)):
            char = s[right]
            freq[char] = freq.get(char, 0) + 1

            while freq[char] > 1:
                freq[s[left]] -= 1
                left += 1

            max_lenght = max(max_lenght, right - left + 1)

        return max_lenght



        

        
        