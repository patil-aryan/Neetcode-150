"""
Climb Stairs Problem - https://leetcode.com/problems/climbing-stairs/
====================

Problem Statement
-----------------
You are climbing a staircase that has `n` steps. You can either climb 1 or 2 steps at a time. 
Return the number of distinct ways you can climb to the top.

Example 1:
    Input: n = 2
    Output: 2
    Explanation: 
        1. 1 step + 1 step
        2. 2 steps

Example 2:
    Input: n = 3
    Output: 3
    Explanation: 
        1. 1 step + 1 step + 1 step
        2. 1 step + 2 steps
        3. 2 steps + 1 step

Constraints:
    - 1 <= n <= 45

Explanation
-----------
This is a dynamic programming problem similar to the Fibonacci sequence. The number of ways to 
climb `n` stairs is the sum of ways to climb `n-1` stairs (take 1 step) and `n-2` stairs (take 
2 steps). We optimize space by only tracking the last two values instead of a full DP array.

Logic of Solution
-----------------
1. Base Cases: If n < 2, return n (0 for n=0, 1 for n=1).
2. Initialize dp = [1, 1] representing ways to reach steps 0 and 1.
3. For each step from 2 to n:
   - Compute new ways as dp[0] + dp[1].
   - Shift values: dp[0] becomes old dp[1], dp[1] becomes new value.
4. Return dp[1].

Time and Space Complexity
-------------------------
- Time Complexity: O(n) - Single loop from 2 to n.
- Space Complexity: O(1) - Constant space with a 2-element list.

-------------------------

Solution - 

"""

class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Calculate the number of distinct ways to climb n stairs taking 1 or 2 steps at a time.
        
        Args:
            n (int): Number of stairs
        Returns:
            int: Number of distinct ways to reach the top
        """
        if n < 2:
            return n
        
        dp = [1, 1]  # dp[0] = ways to step 0, dp[1] = ways to step 1
        i = 2
        while i <= n:
            temp = dp[1]          # Store current dp[1]
            dp[1] = dp[0] + dp[1]  # New ways = ways from n-1 + n-2
            dp[0] = temp          # Shift previous value
            i += 1
        return dp[1]
    


"""

Detailed Dry Run
----------------
Example 1: n = 2
    1. Init: dp = [1, 1], i = 2
    2. i = 2:
       - temp = dp[1] = 1
       - dp[1] = dp[0] + dp[1] = 1 + 1 = 2
       - dp[0] = temp = 1
       - dp = [1, 2]
       - i = 3 (loop ends)
    3. Return: dp[1] = 2
    Ways: [1+1, 2]

Example 2: n = 3
    1. Init: dp = [1, 1], i = 2
    2. i = 2:
       - temp = dp[1] = 1
       - dp[1] = 1 + 1 = 2
       - dp[0] = 1
       - dp = [1, 2]
       - i = 3
    3. i = 3:
       - temp = dp[1] = 2
       - dp[1] = 1 + 2 = 3
       - dp[0] = 2
       - dp = [2, 3]
       - i = 4 (loop ends)
    4. Return: dp[1] = 3
    Ways: [1+1+1, 1+2, 2+1]

Notes on Overall Approach
-------------------------
- This solution uses an iterative approach to avoid recursion stack overflow for large n.
- Space is optimized by using two variables instead of an array of size n.
- The logic mirrors Fibonacci, where each step builds on the previous two.
"""



# Test cases
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        (2, 2),  # Expected: 2 ways
        (3, 3),  # Expected: 3 ways
        (4, 5)   # Expected: 5 ways [1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2]
    ]
    for n, expected in test_cases:
        result = sol.climbStairs(n)
        print(f"n = {n}, Result = {result}, Expected = {expected}, "
              f"{'Pass' if result == expected else 'Fail'}")