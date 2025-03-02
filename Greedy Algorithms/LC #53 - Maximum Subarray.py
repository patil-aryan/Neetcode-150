"""
        Problem: Maximum Subarray (NeetCode 150 #53) - https://leetcode.com/problems/maximum-subarray/description/
        
        Description:
        Given an integer array nums, find the subarray with the largest sum and return its sum.
        A subarray is a contiguous part of the array.

        Args:
            nums (List[int]): Array of integers (can be positive, negative, or zero)

        Returns:
            int: The maximum sum of any contiguous subarray

        Solution Approach:
        This solution uses Kadane's Algorithm, a greedy approach that:
        1. Maintains a running sum (`currSum`) of the current subarray
        2. Resets `currSum` to 0 if it becomes negative (starting fresh is better)
        3. Updates the global maximum sum (`maxSum`) whenever `currSum` exceeds it
        4. Iterates through the array once, making local optimal choices

        Time Complexity: O(n) - single pass through the array
        Space Complexity: O(1) - uses only two variables
"""


from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # Initialize maxSum with first element (handles single-element case)
        maxSum = nums[0]
        # Initialize current running sum
        currSum = 0

        # Iterate through each element in the array
        for i in nums:
            # Reset currSum to 0 if negative (no benefit to continue negative sum)
            currSum = max(currSum, 0)
            # Add current element to running sum
            currSum += i
            # Update maxSum if current sum is larger
            maxSum = max(maxSum, currSum)
        
        return maxSum




"""
# Detailed Examples and Walkthroughs

### Example 1: Mixed Positive and Negative Numbers
Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6

Step-by-step:
| Element | currSum (before reset) | currSum (after reset) | currSum (after add) | maxSum | Explanation                                   |
|---------|-----------------------|-----------------------|---------------------|--------|-----------------------------------------------|
| -2      | 0                     | 0                     | -2                  | -2     | Start, maxSum initialized to -2               |
| 1       | -2                    | 0                     | 1                   | 1      | Reset to 0, add 1, update maxSum              |
| -3      | 1                     | 1                     | -2                  | 1      | Add -3, currSum drops but maxSum stays        |
| 4       | -2                    | 0                     | 4                   | 4      | Reset to 0, add 4, update maxSum              |
| -1      | 4                     | 4                     | 3                   | 4      | Add -1, currSum decreases                     |
| 2       | 3                     | 3                     | 5                   | 5      | Add 2, update maxSum                          |
| 1       | 5                     | 5                     | 6                   | 6      | Add 1, update maxSum (peak)                   |
| -5      | 6                     | 6                     | 1                   | 6      | Add -5, currSum drops but maxSum holds        |
| 4       | 1                     | 1                     | 5                   | 6      | Add 4, currSum rises but doesn’t beat maxSum  |

Subarray Visualization:
[-2, 1, -3, [4, -1, 2, 1], -5, 4]
Sum = 4 + (-1) + 2 + 1 = 6
Result: maxSum = 6

# Detailed Examples and Walkthroughs

### Example 1: Mixed Positive and Negative Numbers
Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6

Step-by-step:
- Start with maxSum = -2 (first element) and currSum = 0.
- Element -2: currSum = max(0, 0) = 0, then currSum += -2 = -2, maxSum = max(-2, -2) = -2.
- Element 1: currSum = max(-2, 0) = 0, then currSum += 1 = 1, maxSum = max(-2, 1) = 1.
- Element -3: currSum = max(1, 0) = 1, then currSum += -3 = -2, maxSum = max(1, -2) = 1.
- Element 4: currSum = max(-2, 0) = 0, then currSum += 4 = 4, maxSum = max(1, 4) = 4.
- Element -1: currSum = max(4, 0) = 4, then currSum += -1 = 3, maxSum = max(4, 3) = 4.
- Element 2: currSum = max(3, 0) = 3, then currSum += 2 = 5, maxSum = max(4, 5) = 5.
- Element 1: currSum = max(5, 0) = 5, then currSum += 1 = 6, maxSum = max(5, 6) = 6.
- Element -5: currSum = max(6, 0) = 6, then currSum += -5 = 1, maxSum = max(6, 1) = 6.
- Element 4: currSum = max(1, 0) = 1, then currSum += 4 = 5, maxSum = max(6, 5) = 6.

Subarray Visualization:
[-2, 1, -3, [4, -1, 2, 1], -5, 4]
Sum = 4 + (-1) + 2 + 1 = 6
Result: maxSum = 6

### Example 2: All Negative Numbers
Input: nums = [-2, -1, -3]
Output: -1

Step-by-step:
- Start with maxSum = -2 (first element) and currSum = 0.
- Element -2: currSum = max(0, 0) = 0, then currSum += -2 = -2, maxSum = max(-2, -2) = -2.
- Element -1: currSum = max(-2, 0) = 0, then currSum += -1 = -1, maxSum = max(-2, -1) = -1.
- Element -3: currSum = max(-1, 0) = 0, then currSum += -3 = -3, maxSum = max(-1, -3) = -1.

Subarray Visualization:
[-2, [-1], -3]
Sum = -1
Result: maxSum = -1

---

# Additional Notes
Key Insights:
1. Kadane’s Algorithm: Greedily decides at each step whether to start a new subarray 
   (reset to 0) or continue the current one, ensuring the maximum sum.
2. Negative Reset: Dropping a negative `currSum` is optimal because it can’t contribute 
   to a larger sum later.
3. Single Pass: Efficiently finds the maximum by updating `maxSum` on the fly.

Common Pitfalls:
1. Initial Value: Must initialize `maxSum` to first element, not 0, to handle all-negative cases.
2. Reset Logic: Forgetting to reset `currSum` to 0 leads to incorrect results.
3. Subarray Definition: Must be contiguous, not just any subset.

This solution is optimal because:
- Linear time complexity (O(n))
- Constant space (O(1))
- Simple and intuitive implementation
- Handles all cases (positive, negative, mixed, single-element)
"""

# Test Cases
def test_max_subarray():
    """
    Test cases to verify the solution works correctly
    """
    solution = Solution()
    
    # Test Case 1: Mixed positive and negative numbers
    assert solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6, "Test case 1 failed"
    
    # Test Case 2: All negative numbers
    assert solution.maxSubArray([-2, -1, -3]) == -1, "Test case 2 failed"
    
    # Test Case 3: Single element (positive)
    assert solution.maxSubArray([5]) == 5, "Test case 3 failed"
    
    # Test Case 4: Single element (negative)
    assert solution.maxSubArray([-1]) == -1, "Test case 4 failed"
    
    # Test Case 5: All positive numbers
    assert solution.maxSubArray([1, 2, 3, 4]) == 10, "Test case 5 failed"
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_max_subarray()
