"""
Problem Name: LC 200 - Number of Islands

https://leetcode.com/problems/number-of-islands/

Problem Description:
Given a 2D grid of '1's (land) and '0's (water), return the number of islands. An island is a group of connected '1's (horizontally or vertically) surrounded by water. Assume all four edges of the grid are surrounded by water.

Example:
Input: grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
Output: 3

Approach and Explanation:
To count islands, we need to identify distinct groups of connected '1's. We'll use BFS:
1. Scan every cell in the grid.
2. When we hit an unvisited '1', use BFS to explore all connected land cells (up, down, left, right).
3. Mark each visited cell to avoid recounting it.
4. Each time we start a new BFS, it means we've found a new island, so increment the counter.
5. BFS uses a queue to process cells level-by-level, ensuring we fully explore one island before moving to the next.

Why BFS? It systematically floods each island, marking all connected land in one go, which is perfect for grouping.

Time Complexity: O(rows * cols) - we visit each cell at most once, and BFS operations per cell are constant.
Space Complexity: O(rows * cols) - worst case, the queue and visited set store nearly all cells (e.g., all land).

Code:
"""
from collections import deque
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0
        directions = [[0,1], [0,-1], [1,0], [-1,0]]  # right, left, down, up
        
        def bfs(r, c):
            q = deque([(r, c)])  # Start queue with initial cell
            visit.add((r, c))    # Mark starting point as visited
            
            while q:
                row, col = q.popleft()  # Process current cell
                # Explore all 4 directions
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc  # New coordinates
                    # Check if new position is valid
                    if (nr in range(rows) and 
                        nc in range(cols) and 
                        grid[nr][nc] == '1' and 
                        (nr, nc) not in visit):
                        q.append((nr, nc))  # Add to queue
                        visit.add((nr, nc))  # Mark as visited
        
        # Scan grid for unvisited land
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visit:
                    bfs(r, c)  # Explore entire island
                    islands += 1  # Count new island
                    
        return islands

"""
Dry Run 1:
Grid: [
    ["1","1","0"],
    ["0","1","0"],
    ["0","0","1"]
]
Step-by-step:
1. Start at (0,0)='1', visit={(0,0)}, q=[(0,0)], islands=0
   - Pop (0,0): Check neighbors
   - Right (0,1)='1': q=[(0,1)], visit={(0,0),(0,1)}
   - Left/Up: Out of bounds, Down (1,0)='0'
   - Pop (0,1): Right/Left/Up: None, Down (1,1)='1': q=[(1,1)], visit={(0,0),(0,1),(1,1)}
   - Pop (1,1): No new '1's, q=[]
   - BFS done, islands=1
2. Scan to (2,2)='1', visit={(0,0),(0,1),(1,1),(2,2)}, q=[(2,2)], islands=1
   - Pop (2,2): No new '1's, q=[]
   - BFS done, islands=2
3. No more unvisited '1's
Output: 2

Dry Run 2:
Grid: [
    ["1","0","1"],
    ["0","0","0"],
    ["1","0","1"]
]
Step-by-step:
1. (0,0)='1': q=[(0,0)], visit={(0,0)}
   - Pop (0,0): No adjacent '1's, q=[]
   - islands=1
2. (0,2)='1': q=[(0,2)], visit={(0,0),(0,2)}
   - Pop (0,2): No adjacent '1's, q=[]
   - islands=2
3. (2,0)='1': q=[(2,0)], visit={(0,0),(0,2),(2,0)}
   - Pop (2,0): No adjacent '1's, q=[]
   - islands=3
4. (2,2)='1': q=[(2,2)], visit={(0,0),(0,2),(2,0),(2,2)}
   - Pop (2,2): No adjacent '1's, q=[]
   - islands=4
Output: 4

Notes:
- Visited set prevents cycles and double-counting.
- Could use DFS instead of BFS—same complexity, just different traversal order.
- In-place marking (changing '1' to '0') saves space but modifies input.
- Tuple (r,c) in visit set since lists aren't hashable.
"""