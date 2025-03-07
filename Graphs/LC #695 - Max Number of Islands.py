"""
Problem Name: 
LC 695 - Maximum Area of Island
https://leetcode.com/problems/max-area-of-island/

Problem Description:
Given a 2D grid of 1's (land) and 0's (water), return the maximum area of an island. An island is a group of 1's connected 4-directionally (horizontally or vertically). If there are no islands, return 0.

Example:
Input: grid = [
    [0,0,1,0,0],
    [0,0,1,1,0],
    [0,1,1,0,0],
    [0,0,0,0,1]
]
Output: 4
Explanation: The largest island has 4 connected 1's.

Approach and Explanation:
We need to find the largest group of connected 1's in the grid. 

1. Compute the area (number of 1's) for each island and track the maximum.
2. Use Depth-First Search (DFS) to explore and count connected land cells.
3. DFS:
   - Start at a cell with a 1 that hasn’t been visited.
   - Recursively explore all 4 adjacent cells (up, down, left, right).
   - For each valid land cell (1), add 1 to the area and continue exploring its neighbors.
   - Stop when we hit water (0), grid boundaries, or a visited cell.
   - The recursion naturally "floods" the entire island, summing up all connected 1's.
4. Tracking:
   - Use a visited set to mark cells we’ve counted, preventing overlap or infinite loops.
   - Compare each island’s area to a running maximum.
5. Process:
   - Scan the grid cell by cell.
   - When we find an unvisited 1, trigger DFS to compute that island’s area.
   - Update max_area if the current island is larger.

Detailed Logic Breakdown:
- Imagine the grid as a map. Each 1 is land, and we’re measuring the size of each landmass.
- DFS acts like a surveyor: starting at one piece of land, it walks in all directions, counting each connected piece until it can’t go further (hits water or edges).
- The recursive calls stack up: for each cell, we ask, “How many more 1’s are connected below me? Above me? Left? Right?” The answers add up to the total area.
- We only count a cell once (via the visited set), ensuring accuracy.
- By scanning the whole grid, we guarantee we check every possible island and find the biggest one.

Why DFS? It’s perfect for this because:
- It explores deeply in one direction before backtracking, naturally grouping all connected cells.
- The recursion handles the counting automatically—each call contributes its 1 to the total.

Time Complexity: O(rows * cols) - we visit each cell at most once; DFS explores each direction in constant time.
Space Complexity: O(rows * cols) - recursion stack and visited set could grow to grid size if it’s all 1’s.

Code:
"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        max_area = 0
        
        def dfs(r, c):
            # Base cases: out of bounds, visited, or water
            if (min(r, c) < 0 or 
                r == rows or 
                c == cols or 
                (r, c) in visit or 
                grid[r][c] == 0):
                return 0
            visit.add((r, c))  # Mark current cell as visited
            # Count this cell (1) plus all connected land in 4 directions
            return (1 + dfs(r + 1, c) +  # Down
                       dfs(r - 1, c) +   # Up
                       dfs(r, c + 1) +   # Right
                       dfs(r, c - 1))    # Left
        
        # Scan grid for unvisited land
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    area = dfs(r, c)  # Compute area of current island
                    max_area = max(max_area, area)  # Update max
                    
        return max_area

"""
Dry Run 1:
Grid: [
    [0,0,1],
    [1,1,1],
    [0,1,0]
]
Step-by-step:
1. Start at (0,2)=1, visit={(0,2)}, max_area=0
   - DFS(0,2): Check all directions
     - Down DFS(1,2): 1, visit={(0,2),(1,2)}
       - Down DFS(2,2): 0 (water)
       - Up DFS(0,2): 0 (visited)
       - Right DFS(1,3): 0 (out of bounds)
       - Left DFS(1,1): 1, visit={(0,2),(1,2),(1,1)}
         - Down DFS(2,1): 0 (water)
         - Up DFS(0,1): 0 (water)
         - Right DFS(1,2): 0 (visited)
         - Left DFS(1,0): 1, visit={(0,2),(1,2),(1,1),(1,0)}
           - Down DFS(2,0): 0 (water)
           - Up DFS(0,0): 0 (water)
           - Right DFS(1,1): 0 (visited)
           - Left DFS(1,-1): 0 (out of bounds)
           - Returns 1
         - Returns 1 + 1 = 2
       - Returns 1 + 2 = 3
     - Up DFS(-1,2): 0 (out of bounds)
     - Right DFS(0,3): 0 (out of bounds)
     - Left DFS(0,1): 0 (water)
     - Returns 1 + 3 = 4
   - area = 4, max_area = max(0, 4) = 4
2. No unvisited 1’s left
Output: 4

Dry Run 2:
Grid: [
    [1,0,1],
    [0,0,0],
    [1,0,1]
]
Step-by-step:
1. (0,0)=1: visit={(0,0)}, DFS(0,0)=1 (no neighbors), max_area=1
2. (0,2)=1: visit={(0,0),(0,2)}, DFS(0,2)=1 (no neighbors), max_area=1
3. (2,0)=1: visit={(0,0),(0,2),(2,0)}, DFS(2,0)=1 (no neighbors), max_area=1
4. (2,2)=1: visit={(0,0),(0,2),(2,0),(2,2)}, DFS(2,2)=1 (no neighbors), max_area=1
Output: 1

Notes:
- DFS recursion simplifies counting by stacking calls—each returns its contribution to the total.
- Could use BFS with a queue, but DFS is more concise here.
- `min(r,c) < 0` is a shorthand for `r < 0 or c < 0`; separate checks might be clearer.
- Visited set is critical to avoid infinite recursion.
"""