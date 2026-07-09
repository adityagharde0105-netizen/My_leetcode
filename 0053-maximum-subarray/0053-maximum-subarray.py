class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_array = nums[0] # Kadane’s Algorithm
        current_array = nums[0]

        for num in nums[1:]:
            current_array = max(num, current_array + num)
            max_array = max(current_array, max_array)
        return max_array

