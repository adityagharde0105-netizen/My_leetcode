class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr = []
        total = 0

        for i in nums:
            total += i
            arr.append(total)
        return arr

        