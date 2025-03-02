"""
Problem Statement and Explanation:
You are given a network of n nodes labeled from 1 to n, a list of travel times as directed edges times[i] = [u, v, w]
where u is the source node, v is the target node, and w is the time taken to travel from u to v, and an integer k as the
starting node. Find the minimum time required for all nodes to receive a signal sent from node k. If it’s impossible
for all nodes to receive the signal, return -1.

Example:
- Input: times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]], n = 4, k = 2
- Output: 2
- Explanation: Signal from node 2 reaches:
  - Node 1 at time 1 (2 -> 1, weight 1)
  - Node 3 at time 1 (2 -> 3, weight 1)
  - Node 4 at time 2 (2 -> 3 -> 4, weights 1 + 1)
  - Max time = 2, all nodes reached.

Logic and Approach:
This solution implements Dijkstra’s Algorithm to find the shortest path from the starting node k to all other nodes:
1. Adjacency List Construction:
   - Build a graph as an adjacency list where adj[u] contains pairs [v, w] for each edge u -> v with weight w.
2. Min-Heap Initialization:
   - Use a priority queue (min-heap) to store tuples (distance, node), starting with (0, k) since the distance to k is 0.
3. Shortest Path Tracking:
   - Maintain a dictionary 'shortest' to store the minimum time to reach each node from k.
4. Dijkstra’s Core Loop:
   - While the heap is not empty:
     - Pop the node u1 with the smallest distance w1.
     - If u1 is already in 'shortest', skip it (we’ve found a shorter path already).
     - Record w1 as the shortest time to u1.
     - For each neighbor u2 of u1 with weight w2:
       - If u2 isn’t in 'shortest', add (w1 + w2, u2) to the heap to explore its path.
5. Result Check:
   - If 'shortest' contains all n nodes, return the maximum value (longest shortest path).
   - Otherwise, return -1 (not all nodes are reachable).

Detailed Logic (Dijkstra’s Algorithm):
- Dijkstra’s Algorithm finds the shortest path from a single source to all destinations in a weighted graph with non-negative weights.
- Key Idea: Greedily select the unvisited node with the smallest known distance from the source, update its neighbors’ distances, and mark it visited.
- Here’s how it applies:
  - Min-Heap ensures we always process the node with the smallest current distance first (greedy choice).
  - 'shortest' acts as the visited set and stores final distances, avoiding reprocessing nodes with known shortest paths.
  - For each node u1, explore neighbors u2, updating their tentative distances (w1 + w2) if shorter.
- Why It Works: The heap guarantees that once a node’s shortest distance is finalized (popped and added to 'shortest'), no shorter path exists due to the non-negative weights (triangle inequality).

Time and Space Complexity:
- Time Complexity: O((V + E) log V)
  - V = number of nodes (n), E = number of edges (len(times)).
  - Heap operations: O(log V) for push/pop, performed O(V + E) times.
- Space Complexity: O(V + E)
  - Adjacency list: O(E), heap: O(V), shortest dict: O(V).

Actual Code:
"""
import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n + 1):
            adj[i] = []
        
        for u, v, w in times:
            adj[u].append([v, w])

        shortest = {}
        minHeap = [(0, k)]

        while minHeap:
            w1, u1 = heapq.heappop(minHeap)
            if u1 in shortest:
                continue
            shortest[u1] = w1

            for u2, w2 in adj[u1]:
                if u2 not in shortest:
                    heapq.heappush(minHeap, (w1 + w2, u2))

        if len(shortest) == n:
            return max(shortest.values())
        return -1

"""
Dry Run 1: times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]], n = 4, k = 2
- adj = {1: [], 2: [[1, 1], [3, 1]], 3: [[4, 1]], 4: []}
- minHeap = [(0, 2)], shortest = {}
- Iteration 1:
  - Pop (0, 2), shortest = {2: 0}
  - Neighbors: [1, 1], [3, 1]
  - Push (0+1, 1), (0+1, 3) -> minHeap = [(1, 1), (1, 3)]
- Iteration 2:
  - Pop (1, 1), shortest = {2: 0, 1: 1}
  - Neighbors: [] (none)
- Iteration 3:
  - Pop (1, 3), shortest = {2: 0, 1: 1, 3: 1}
  - Neighbors: [4, 1]
  - Push (1+1, 4) -> minHeap = [(2, 4)]
- Iteration 4:
  - Pop (2, 4), shortest = {2: 0, 1: 1, 3: 1, 4: 2}
  - Neighbors: [] (none)
- minHeap empty, len(shortest) = 4 == n, return max(0, 1, 1, 2) = 2
- Explanation: Signal reaches all nodes; longest time is 2 (to node 4).

Dry Run 2: times = [[1, 2, 1]], n = 2, k = 2
- adj = {1: [[2, 1]], 2: []}
- minHeap = [(0, 2)], shortest = {}
- Iteration 1:
  - Pop (0, 2), shortest = {2: 0}
  - Neighbors: [] (none)
- minHeap empty, len(shortest) = 1 < 2, return -1
- Explanation: Node 1 is unreachable from k=2, so return -1.

Notes on the Solution:
- This is a direct application of Dijkstra’s Algorithm optimized with a min-heap for priority queue efficiency.
- The 'shortest' dictionary doubles as a visited set and final distance tracker, avoiding redundant heap entries.
- Non-negative weights ensure the greedy choice (smallest distance first) is optimal.
- Edge case: If k has no outgoing edges and n > 1, it correctly returns -1.
- Could optimize by pre-checking if k can reach all nodes via DFS, but Dijkstra’s suffices for the problem constraints.
"""
