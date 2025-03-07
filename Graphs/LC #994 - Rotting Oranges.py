"""
Problem Name: 
LC #994 - Rotting Oranges
https://leetcode.com/problems/rotting-oranges/

Problem Description:
Given a grid where 0 = empty cell, 1 = fresh orange, 2 = rotten orange, return the minimum minutes until all oranges are rotten. A rotten orange can rot adjacent fresh oranges (4-directionally) each minute. If it’s impossible to rot all oranges, return -1.

Example:
Input: grid = [
    [2,1,1],
    [1,1,0],
    [0,1,1]
]
Output: 4
Explanation: It takes 4 minutes for all fresh oranges to rot.

Approach and Explanation:
To find the minimum time for all oranges to rot, we simulate the rotting process using Breadth-First Search (BFS):

1. Find the minimum time for all fresh oranges to rot, or determine if it’s impossible.
2. Use BFS to spread rot from all rotten oranges simultaneously, minute by minute.
3. Initialization:
   - Count fresh oranges (1’s) to track progress.
   - Queue all initial rotten oranges (2’s) as starting points.
4. BFS Process:
   - Process all oranges in the queue at the current minute (level-by-level BFS).
   - For each rotten orange, check its 4 neighbors.
   - If a neighbor is fresh (1), rot it (set to 2), add it to the queue, and decrease the fresh count.
   - After processing all oranges at the current minute, increment time.
   - Repeat until no fresh oranges remain or the queue is empty.
5. Result:
   - If fresh = 0, return time (all oranges rotted).
   - If fresh > 0, return -1 (some oranges can’t be reached).

Detailed Logic Breakdown:
- Think of the grid as an orange grove. Rotten oranges (2’s) are the source of a "disease" that spreads to fresh oranges (1’s) each minute.
- BFS is ideal because:
  - It processes rot in waves, mimicking the minute-by-minute spread.
  - Starting with all initial 2’s ensures we compute the shortest time (parallel rotting).
- The outer while loop tracks minutes, and the inner for loop handles all oranges rotting at the same time step.
- We modify the grid in-place (1 → 2) to mark oranges as rotten and avoid revisiting them.
- The fresh counter ensures we know when all oranges are done or if some are unreachable (isolated by 0’s or edges).
- Key insight: We only increment time after a full level of rotting, not per orange, because BFS ensures each level is one minute.

Time Complexity: O(rows * cols) - we visit each cell at most once (when it rots).
Space Complexity: O(rows * cols) - the queue could hold nearly all cells in the worst case (e.g., all oranges).

Code:
"""
from collections import deque
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()  # Queue for BFS
        time = 0     # Minutes elapsed
        fresh = 0    # Count of fresh oranges
        
        # Initialize: count fresh and queue rotten oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        
        directions = [[0,1], [0,-1], [1,0], [-1,0]]  # Right, left, down, up
        
        # BFS: spread rot while fresh oranges remain
        while q and fresh > 0:
            # Process all oranges rotting at current minute
            for i in range(len(q)):
                row, col = q.popleft()
                
                # Check 4 adjacent cells
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    
                    # Skip if out of bounds or not fresh
                    if (r < 0 or c < 0 or 
                        r == rows or c == cols or 
                        grid[r][c] != 1):
                        continue
                    
                    # Rot the fresh orange
                    grid[r][c] = 2
                    q.append((r, c))  # Add to queue for next minute
                    fresh -= 1        # One less fresh orange
            
            time += 1  # Increment time after full level
        
        # Return time if all rotted, else -1
        return time if fresh == 0 else -1

"""
Dry Run 1:
Grid: [
    [2,1,1],
    [1,1,0],
    [0,1,1]
]
Step-by-step:
1. Init: fresh=6, q=[(0,0)], time=0
2. Minute 1: q=[(0,0)]
   - Pop (0,0): Check neighbors
     - Right (0,1)=1: Rot to 2, q=[(0,1)], fresh=5
     - Down (1,0)=1: Rot to 2, q=[(0,1),(1,0)], fresh=4
   - time=1
3. Minute 2: q=[(0,1),(1,0)]
   - Pop (0,1): Right (0,2)=1: Rot to 2, q=[(1,0),(0,2)], fresh=3
   - Pop (1,0): Down (2,0)=0, Right (1,1)=1: Rot to 2, q=[(0,2),(1,1)], fresh=2
   - time=2
4. Minute 3: q=[(0,2),(1,1)]
   - Pop (0,2): Down (1,2)=0
   - Pop (1,1): Down (2,1)=1: Rot to 2, q=[(2,1)], fresh=1
   - time=3
5. Minute 4: q=[(2,1)]
   - Pop (2,1): Right (2,2)=1: Rot to 2, q=[(2,2)], fresh=0
   - time=4
6. q=[(2,2)], fresh=0, stop
Output: 4 (fresh=0)

Dry Run 2:
Grid: [
    [2,1,0],
    [0,1,0],
    [1,0,1]
]
Step-by-step:
1. Init: fresh=4, q=[(0,0)], time=0
2. Minute 1: q=[(0,0)]
   - Pop (0,0): Right (0,1)=1: Rot to 2, q=[(0,1)], fresh=3
   - time=1
3. Minute 2: q=[(0,1)]
   - Pop (0,1): Down (1,1)=1: Rot to 2, q=[(1,1)], fresh=2
   - time=2
4. Minute 3: q=[(1,1)]
   - Pop (1,1): No fresh neighbors, q=[]
   - time=3
5. q empty, fresh=2 (at (2,0) and (2,2) unreachable)
Output: -1

Notes:
- BFS ensures minimum time by processing levels (minutes) correctly.
- Modifying grid in-place saves space vs. using a visited set.
- The for loop inside while is key—it groups all rot at the same minute.
- Fresh count tracks completion and detects impossible cases.
"""