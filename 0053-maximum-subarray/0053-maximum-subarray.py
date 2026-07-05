class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_array = nums[0] # Kadane’s Algorithm
        current_array = nums[0]

        for num in nums[1:]:
            current_array = max(num, current_array + num)
            max_array = max(current_array, max_array)
        return max_array

''' For me!!!
nums = [-2, 1, -3, 4]


Step 1: Initialization
current_sum = -2
max_sum = -2
We start from first element.


Step 2: num = 1
Now we decide:
Option 1: start new subarray
1
Option 2: extend previous
current_sum + num = -2 + 1 = -1
Now:
current_sum = max(1, -1) = 1
Update max:
max_sum = max(-2, 1) = 1


Step 3: num = -3
Option 1: start new
-3
Option 2: extend
1 + (-3) = -2
So:
current_sum = max(-3, -2) = -2
Update:
max_sum = max(1, -2) = 1


Step 4: num = 4
Option 1: start new
4
Option 2: extend
-2 + 4 = 2
So:
current_sum = max(4, 2) = 4
Update:
max_sum = max(1, 4) = 4
Final answer = 4'''


        