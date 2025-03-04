"""
LC 146 - LRU Cache 

Source: https://leetcode.com/problems/lru-cache/description/

=================

Problem Statement
-----------------
Design a data structure that implements an LRU (Least Recently Used) Cache with the following operations:
1. `LRUCache(int capacity)`: Initialize the LRU cache with a positive capacity.
2. `int get(int key)`: Return the value of the key if it exists, otherwise return -1. Move the accessed key to the most recently used position.
3. `void put(int key, int value)`: Update the value of the key if it exists, or insert the key-value pair if it doesn't. If the cache exceeds capacity, remove the least recently used item.

Example:
    LRUCache cache = new LRUCache(2);
    cache.put(1, 1);    // cache is {1=1}
    cache.put(2, 2);    // cache is {1=1, 2=2}
    cache.get(1);       // returns 1, cache is {2=2, 1=1}
    cache.put(3, 3);    // removes key 2, cache is {1=1, 3=3}
    cache.get(2);       // returns -1 (not found)
    cache.put(4, 4);    // removes key 1, cache is {3=3, 4=4}
    cache.get(1);       // returns -1 (not found)

Constraints:
    - 1 <= capacity <= 3000
    - 0 <= key <= 10^4
    - 0 <= value <= 10^5
    - At most 2 * 10^5 calls will be made to get and put.

Explanation
-----------
The LRU Cache combines a doubly linked list and a hash map:
- Doubly Linked List: Tracks the order of elements from least recently used (LRU) to most recently used (MRU). Dummy nodes `left` and `right` act as sentinels to simplify operations.
- Hash Map: Maps keys to their corresponding nodes in the list for O(1) access.

Key operations:
- Get: Fetch value, promote node to MRU.
- Put: Insert or update node at MRU, evict LRU if necessary.

Logic of Solution
-----------------
The design leverages two data structures for efficiency:

1. Node Class:
   - Represents a key-value pair with `prev` and `next` pointers, forming the doubly linked list.
   - Each node stores `key` and `val` to allow removal from the hash map when evicted.

2. LRUCache Initialization:
   - Set `capacity` to limit the cache size.
   - Initialize an empty hash map (`cache`) to store key-node pairs.
   - Create dummy nodes `left` (before LRU) and `right` (after MRU), linked as `left <-> right`.
   - This setup ensures the list is never truly empty, simplifying edge cases.

3. Remove Helper:
   - Goal: Detach a node from its current position in the list.
   - Logic: Given a node, connect its `prev` to its `next`, bypassing the node.
   - Example: For `A <-> B <-> C`, removing `B` updates `A.next = C` and `C.prev = A`.

4. Insert Helper:
   - Goal: Add a node at the MRU position (just before `right`).
   - Logic: Link the node between `right.prev` (current MRU) and `right`.
   - Steps: Update pointers of `prev`, `nxt`, and the new node to maintain the chain.
   - Example: Inserting `D` into `left <-> C <-> right` becomes `left <-> C <-> D <-> right`.

5. Get Method:
   - Goal: Retrieve a value and mark it as most recently used.
   - Logic:
     - Check if `key` exists in `cache`.
     - If yes, remove the node from its current position (via `remove`), insert it at MRU (via `insert`), and return its value.
     - If no, return -1.
   - This ensures accessed items move to the front of the usage order.

6. Put Method:
   - Goal: Insert or update a key-value pair, evict LRU if over capacity.
   - Logic:
     - If `key` exists, remove its old node to avoid duplicates.
     - Create a new node with the key-value pair, add to `cache`, and insert at MRU.
     - If `len(cache) > capacity`, identify the LRU (node after `left`), remove it from the list, and delete its key from `cache`.
   - This maintains the cache within its size limit, evicting the least used item.

Time and Space Complexity
-------------------------
- Time Complexity: O(1) for `get` and `put`:
  - Hash map lookups: O(1).
  - List operations (`remove`, `insert`): O(1) due to direct pointer manipulation.
- Space Complexity: O(capacity):
  - Hash map stores up to `capacity` key-node pairs.
  - Linked list stores up to `capacity` nodes plus two dummy nodes.

-------------------------

Solution -

"""

class Node:
    def __init__(self, key, value):
        """Initialize a doubly linked list node with key and value."""
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        """
        Initialize the LRU Cache with given capacity.
        
        Args:
            capacity (int): Maximum number of key-value pairs the cache can hold.
        """
        self.cap = capacity
        self.cache = {}  # Hash map: key -> Node
        
        # Dummy nodes: left (LRU side), right (MRU side)
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        """Remove a node from the doubly linked list."""
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        """Insert a node at the MRU position (just before right)."""
        prev, nxt = self.right.prev, self.right
        prev.next, nxt.prev = node, node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        """
        Get the value of the key if it exists, move it to MRU, else return -1.
        
        Args:
            key (int): Key to look up.
        Returns:
            int: Value if key exists, -1 otherwise.
        """
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        """
        Insert or update a key-value pair, evict LRU if over capacity.
        
        Args:
            key (int): Key to insert or update.
            value (int): Value associated with the key.
        """
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next  # LRU is just after left
            self.remove(lru)
            del self.cache[lru.key]


"""
Detailed Dry Run
----------------
capacity = 2:
1. put(1, 1):
   - Cache: {1: Node(1,1)}
   - List: left <-> Node(1,1) <-> right
2. put(2, 2):
   - Cache: {1: Node(1,1), 2: Node(2,2)}
   - List: left <-> Node(1,1) <-> Node(2,2) <-> right
3. get(1):
   - Remove Node(1,1): left <-> Node(2,2) <-> right
   - Insert Node(1,1): left <-> Node(2,2) <-> Node(1,1) <-> right
   - Return: 1
4. put(3, 3):
   - Over capacity, LRU = Node(2,2)
   - Remove Node(2,2): left <-> Node(1,1) <-> right
   - Delete {2}: Cache = {1: Node(1,1)}
   - Insert Node(3,3): left <-> Node(1,1) <-> Node(3,3) <-> right
   - Cache: {1: Node(1,1), 3: Node(3,3)}

Notes on Overall Approach
-------------------------
- Why Doubly Linked List?: 
  - Singly linked lists require O(n) to remove a node (need previous node), but doubly linked lists allow O(1) removal with `prev` pointers.
  - Direct access to neighbors simplifies insertion and deletion logic.

- Why Hash Map?: 
  - Without it, finding a node by key would be O(n) in a list. The hash map provides O(1) lookup, mapping keys to nodes.

- Dummy Nodes:
  - `left` and `right` act as sentinels, avoiding special cases (e.g., empty list, inserting/removing at ends).
  - Example: Inserting into an empty list (`left <-> right`) becomes `left <-> node <-> right` without extra checks.

- MRU/LRU Placement:
  - MRU near `right` and LRU near `left` provide a clear, consistent order.
  - Moving nodes to MRU on access ensures the least used are always near `left`.

- Trade-offs:
  - Space overhead of two pointers per node and dummy nodes is justified by O(1) time complexity.
  - Alternative (e.g., array + queue) would require O(n) shifting or less intuitive logic.

- Greedy Eviction:
  - Evicting LRU on overflow is optimal for the LRU policy, ensuring the most recently used items are retained.
"""



