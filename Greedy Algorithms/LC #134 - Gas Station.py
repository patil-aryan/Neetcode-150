"""


Leectcode 134 - Gas Station - https://leetcode.com/problems/gas-station/description/

Problem Statement and Explanation:
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
You have a car with an unlimited gas tank, and it costs cost[i] of gas to travel from the ith station 
to the (i+1)th station. You begin the journey with an empty tank at one of the gas stations.
Return the starting gas station's index if you can travel around the circuit once in the clockwise 
direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.

Example:
gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
- Start at station 3 (index 3): tank = 0 + 4 = 4
- To station 4: tank = 4 - 1 + 5 = 8
- To station 0: tank = 8 - 2 + 1 = 7
- To station 1: tank = 7 - 3 + 2 = 6
- To station 2: tank = 6 - 4 + 3 = 5
- To station 3: tank = 5 - 5 + 4 = 4 (completes circuit)

Logic and Approach:
1. If the total gas available (sum(gas)) is less than the total gas required (sum(cost)), 
   it’s impossible to complete the circuit. Return -1.
2. Use a greedy approach: track the running total of gas remaining (total) as we visit each station.
3. If at any point total becomes negative, the current starting point won’t work. Reset total to 0 
   and move the start point to the next station (i + 1).
4. Since the solution is unique and the array is circular, if sum(gas) >= sum(cost), the last 
   start point we settle on will be valid.

Time and Space Complexity:
- Time Complexity: O(n) - Single pass through the gas and cost arrays.
- Space Complexity: O(1) - Only use a few variables (total, start), no extra data structures.

Actual Code:
"""
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):  # Check if total gas is less than total cost
            return -1
        
        total = 0  # Running total of gas remaining
        start = 0  # Starting station index
        
        for i in range(len(gas)):
            total += gas[i] - cost[i]  # Update total with net gas at each station
            
            if total < 0:  # If total goes negative, this start point fails
                start = i + 1  # Move start to next station
                total = 0  # Reset total
        
        return start  # Return the valid starting point

"""
Dry Run 1: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
- sum(gas) = 15, sum(cost) = 15, 15 >= 15, so proceed.
- i=0: total = 0 + (1-3) = -2, total < 0, start = 1, total = 0
- i=1: total = 0 + (2-4) = -2, total < 0, start = 2, total = 0
- i=2: total = 0 + (3-5) = -2, total < 0, start = 3, total = 0
- i=3: total = 0 + (4-1) = 3, total >= 0, continue
- i=4: total = 3 + (5-2) = 6, total >= 0, continue
- Loop ends, start = 3, return 3
Explanation: Starting at index 3 allows completion as total never goes negative from there.

Dry Run 2: gas = [2,3,4], cost = [3,4,3]
- sum(gas) = 9, sum(cost) = 10, 9 < 10, return -1
Explanation: Total gas is less than total cost, so no solution exists.

Notes on the Solution:
- The solution leverages the fact that if a solution exists, it’s unique, and the total gas must 
  at least equal the total cost.
- The greedy reset of the start point works because if you can’t proceed from a station, no 
  prior station can be the answer (since total would’ve gone negative earlier).
- This avoids simulating the full circuit from each starting point, optimizing to O(n).
"""