"""
# Jump Game II (NeetCode 150 #45) - https://leetcode.com/problems/jump-game-ii/description/

## Problem Statement
Given an array of non-negative integers where each element represents your maximum 
jump length at that position, return the minimum number of jumps to reach the last 
index from the first index (index 0). You can assume the last index is always reachable.

- Input: Array of integers (e.g., [2, 3, 1, 1, 4])
- Output: Integer (minimum number of jumps to reach the last index)
- Constraints:
  - 1 <= nums.length <= 10^4
  - 0 <= nums[i] <= 1000

Example:
- Input: [2, 3, 1, 1, 4]
- Output: 2
- Explanation: Minimum jumps are 0 → 1 → 4 (2 jumps)

---

## Approach
- Strategy: Greedy (Forward Traversal with Jump Window)
- Core Idea: Minimize jumps by maximizing the reach of each jump, using a window of 
  current reach (`end`) and potential next reach (`far`).
- Steps:
  1. Initialize `count` (jumps), `far` (farthest reachable), and `end` (current jump boundary) to 0.
  2. Iterate from index 0 to len(nums) - 2:
     - Update `far` to the maximum reachable index from current position.
     - When we reach the current boundary (`i == end`), take a jump:
       - Increment `count`.
       - Set `end` to `far` (new boundary).
  3. Return `count` as the minimum jumps needed.

The greedy choice is to jump only when necessary (at `end`) and to the farthest 
reachable point, ensuring the minimum number of jumps.

---

## Time Complexity
- O(n): Single pass through the array (excluding the last index), where n is the length of nums.
- Each element is processed exactly once.

## Space Complexity
- O(1): Uses only three variables (`count`, `far`, `end`) regardless of input size.

---

## Solution
The code below implements the greedy approach with inline comments for clarity.

"""
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Returns the minimum number of jumps to reach the last index.

        Args:
            nums (List[int]): Array of non-negative integers where each value is
                            the maximum jump length from that position

        Returns:
            int: Minimum number of jumps required
        """
        # Initialize jumps counter and reach variables
        count = 0          # Number of jumps taken
        far = 0            # Farthest index reachable with one more jump
        end = 0            # Current jump window boundary

        # Iterate until second-to-last element
        for i in range(len(nums) - 1):
            # Update farthest reachable index
            far = max(far, nums[i] + i)
            
            # If we’ve reached the current boundary, take a jump
            if i == end:
                count += 1     # Increment jump count
                end = far      # Update boundary to farthest reach

        return count

""""

## Dry Runs

### Example 1: Standard Case
Input: [2, 3, 1, 1, 4]
Output: 2

Step-by-Step:
| i | nums[i] | far (before) | far (after) | end (before) | end (after) | count | Explanation                                      |
|---|---------|--------------|-------------|--------------|-------------|-------|--------------------------------------------------|
| 0 | 2       | 0            | 2           | 0            | 2           | 1     | far = max(0, 0+2) = 2, i == end, jump to 2      |
| 1 | 3       | 2            | 4           | 2            | 2           | 1     | far = max(2, 1+3) = 4, no jump yet              |
| 2 | 1       | 4            | 4           | 2            | 4           | 2     | far = max(4, 2+1) = 4, i == end, jump to 4      |
| 3 | 1       | 4            | 4           | 4            | 4           | 2     | far = max(4, 3+1) = 4, no jump needed           |

Path Visualization:
[2] -> [3] -> [1] -> [1] -> [4]
 0      1      2      3      4
Jumps: 0 → 1 → 4 (2 jumps)
Result: count = 2

### Example 2: Edge Case with Zero
Input: [2, 3, 0, 1, 4]
Output: 2

Step-by-Step:
| i | nums[i] | far (before) | far (after) | end (before) | end (after) | count | Explanation                                      |
|---|---------|--------------|-------------|--------------|-------------|-------|--------------------------------------------------|
| 0 | 2       | 0            | 2           | 0            | 2           | 1     | far = max(0, 0+2) = 2, i == end, jump to 2      |
| 1 | 3       | 2            | 4           | 2            | 2           | 1     | far = max(2, 1+3) = 4, no jump yet              |
| 2 | 0       | 4            | 4           | 2            | 4           | 2     | far = max(4, 2+0) = 4, i == end, jump to 4      |
| 3 | 1       | 4            | 4           | 4            | 4           | 2     | far = max(4, 3+1) = 4, no jump needed           |

Path Visualization:
[2] -> [3] -> [0] -> [1] -> [4]
 0      1      2      3      4
Jumps: 0 → 1 → 4 (2 jumps)
Result: count = 2

---

## Notes
- Greedy Justification: By jumping to the farthest reachable point when we hit `end`, 
  we ensure minimal jumps, as we maximize coverage per jump.
- Why `i == end`: This condition triggers a jump when we’ve exhausted the current 
  jump’s range, timing the increment of `count` perfectly.
- Edge Cases: 
  - Single-element array returns 0 (loop doesn’t run).
  - Zeros don’t block progress if a prior jump can bypass them.
- Difference from Jump Game I: While Jump Game I checks reachability (boolean), 
  Jump Game II counts minimum jumps (integer), requiring a forward approach to track steps.
- Optimization: No need for extra checks since the problem guarantees reachability.
"""



# Test cases for verification
def test_solution():
    """
    Runs test cases to ensure the solution works correctly.
    """
    sol = Solution()
    
    # Test 1: Standard case - 2 jumps
    assert sol.jump([2, 3, 1, 1, 4]) == 2, "Test 1 failed"
    
    # Test 2: Zero in middle - still 2 jumps
    assert sol.jump([2, 3, 0, 1, 4]) == 2, "Test 2 failed"
    
    # Test 3: Single element - 0 jumps
    assert sol.jump([1]) == 0, "Test 3 failed"
    
    # Test 4: All ones - jumps equal to length-1
    assert sol.jump([1, 1, 1, 1]) == 3, "Test 4 failed"
    
    # Test 5: Large jumps - 1 jump possible
    assert sol.jump([5, 1, 1, 1, 1]) == 1, "Test 5 failed"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
