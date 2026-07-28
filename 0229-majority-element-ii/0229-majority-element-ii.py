class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        answer = []
        n = len(nums)

        for num in freq:
            if freq[num] > n // 3:
                answer.append(num)

        return answer
        