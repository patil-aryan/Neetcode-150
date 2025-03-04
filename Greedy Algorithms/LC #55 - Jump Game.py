from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Problem: Jump Game (NeetCode 150 #55) - https://leetcode.com/problems/jump-game/
        
        Description:
        Given an array of non-negative integers where each element represents your maximum 
        jump length at that position, determine if you can reach the last index starting 
        from the first index (index 0).

        Args:
            nums (List[int]): Array of non-negative integers representing max jump lengths

        Returns:
            bool: True if the last index can be reached, False otherwise

        Solution Approach:
        This solution uses a greedy algorithm that works backwards from the end:
        1. Start with the goal as the last index
        2. Iterate backwards through the array
        3. For each position, check if we can reach or exceed the current goal
        4. If we can reach the goal, update goal to current position
        5. Return true if we can reach index 0, false otherwise

        Time Complexity: O(n) - single pass through the array
        Space Complexity: O(1) - uses only one variable
        """
        # Initialize goal as the last index
        goal = len(nums) - 1
        
        # Iterate backwards from second-to-last element to start
        for i in range(len(nums) - 1, -1, -1):
            # If current position can reach or exceed goal
            if i + nums[i] >= goal:
                # Update goal to current position
                goal = i
        
        # Return true if we can reach starting position
        return goal == 0

# Detailed Examples and Walkthroughs
"""
Example 1: Working Case
Input: nums = [2, 3, 1, 1, 4]
Output: True

Step-by-step:
1. goal = 4 (last index)
2. i = 4: 4 + 4 = 8 ≥ 4  → goal = 4
3. i = 3: 3 + 1 = 4 ≥ 4  → goal = 3
4. i = 2: 2 + 1 = 3 ≥ 3  → goal = 2
5. i = 1: 1 + 3 = 4 ≥ 2  → goal = 1
6. i = 0: 0 + 2 = 2 ≥ 1  → goal = 0
Result: goal = 0 → True

Path visualization:
[2] -> [3] -> [1] -> [1] -> [4]
0      1      2      3      4
Possible path: 0(2) -> 1(3) -> 4

Example 2: Non-working Case
Input: nums = [3, 2, 1, 0, 4]
Output: False

Step-by-step:
1. goal = 4 (last index)
2. i = 4: 4 + 4 = 8 ≥ 4  → goal = 4
3. i = 3: 3 + 0 = 3 < 4  → goal = 4
4. i = 2: 2 + 1 = 3 < 4  → goal = 4
5. i = 1: 1 + 2 = 3 < 4  → goal = 4
6. i = 0: 0 + 3 = 3 < 4  → goal = 4
Result: goal = 4 ≠ 0 → False

Path visualization:
[3] -> [2] -> [1] -> [0] -> [4]
0      1      2      3      4
Blocked at index 3 (value 0) - can't reach 4

Edge Case Example:
Input: nums = [0]
Output: True

Step-by-step:
1. goal = 0 (last index)
2. i = 0: 0 + 0 = 0 ≥ 0  → goal = 0
Result: goal = 0 → True
(Already at destination)
"""

# Test Cases
def test_can_jump():
    """
    Test cases to verify the solution works correctly
    """
    solution = Solution()
    
    # Test Case 1: Normal working case
    assert solution.canJump([2, 3, 1, 1, 4]) == True, "Test case 1 failed"
    
    # Test Case 2: Non-working case with zero blocking
    assert solution.canJump([3, 2, 1, 0, 4]) == False, "Test case 2 failed"
    
    # Test Case 3: Single element array
    assert solution.canJump([0]) == True, "Test case 3 failed"
    
    # Test Case 4: Minimum jumps needed
    assert solution.canJump([1, 1, 1, 1]) == True, "Test case 4 failed"
    
    # Test Case 5: Large jumps possible but blocked
    assert solution.canJump([5, 0, 0, 0]) == False, "Test case 5 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_can_jump()

# Additional Notes
"""
Key Insights:
1. Greedy Choice: At each step, we make the locally optimal choice of updating
   the goal when possible, which leads to global solution
2. Backward Approach: Working backwards simplifies the problem by converting
   it to "can we reach this point?" instead of "where can we go?"
3. Robustness: Handles edge cases like single-element arrays and arrays with zeros

Common Pitfalls:
1. Don't confuse array values with indices
2. Remember that you can jump less than the maximum distance
3. Zero values don't necessarily mean failure unless they block all paths

This solution is optimal because:
- Single pass through array (O(n) time)
- Constant extra space (O(1) space)
- Simple to implement and understand
- Handles all edge cases correctly
"""