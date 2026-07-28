class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq =  {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        sorted_num = sorted(freq, key = freq.get, reverse = True)

        answer = []

        for i in range(k):
                answer.append(sorted_num[i])
        return answer

    
        