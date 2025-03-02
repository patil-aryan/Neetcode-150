"""
LC 846 - Hand of Straights 

https://leetcode.com/problems/hand-of-straights/description/

Problem Statement and Explanation:
Alice has a hand of cards represented as an array of integers 'hand'. She wants to rearrange the cards into
groups so that each group is of size 'groupSize' and consists of 'groupSize' consecutive cards. Return 
true if such a rearrangement is possible, false otherwise.

Example:
- Input: hand = [1, 2, 3, 6, 2, 3, 4, 7, 8], groupSize = 3
- Output: true
- Explanation: Can form groups [1, 2, 3], [2, 3, 4], [6, 7, 8], each of size 3 with consecutive numbers.

Logic and Approach:
The solution uses a greedy approach with a min-heap to efficiently form groups of consecutive numbers:
1. Preliminary Check:
   - If len(hand) % groupSize != 0, return False since the total cards must be divisible into groups.
2. Frequency Map:
   - Use Counter to track the frequency of each number in 'hand'.
3. Min-Heap Setup:
   - Create a min-heap from the unique numbers (keys of Counter) to always access the smallest available number.
4. Group Formation:
   - While the heap is not empty:
     - Take the smallest number (min_val = heap[0]) as the start of a potential group.
     - For each number i in range(min_val, min_val + groupSize):
       - If i is not in Counter, return False (missing a consecutive number).
       - Decrement Counter[i] since one instance is used.
       - If Counter[i] reaches 0:
         - If i equals the heap's smallest number (heap[0]), remove it from the heap (heappop).
         - If i is not the smallest number, return False (a larger number was depleted before a smaller one, breaking the greedy order).
5. Completion:
   - If the loop completes without returning False, all cards have been grouped successfully, so return True.

Detailed Logic:
- The min-heap ensures we always start with the smallest available number, which is critical for forming consecutive groups greedily.
- By processing groupSize consecutive numbers each iteration, we simulate forming a group (e.g., [1, 2, 3]).
- The check 'i != minHeap[0]' prevents premature depletion of larger numbers, ensuring the heap reflects the smallest remaining numbers.
- This approach avoids sorting the entire array repeatedly, leveraging the heap's O(log k) operations for efficiency.

Time and Space Complexity:
- Time Complexity: O(n log k)
  - n = len(hand), k = number of unique elements in hand.
  - Heapify: O(k), heappop: O(log k), and we process each of n elements across all groups.
- Space Complexity: O(k)
  - Counter and minHeap store at most k unique elements.

Actual Code:
"""
from collections import Counter
import heapq
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        counter = Counter(hand)
        minHeap = list(counter.keys())
        heapq.heapify(minHeap)

        while minHeap:
            min_val = minHeap[0]
            for i in range(min_val, min_val + groupSize):
                if i not in counter:
                    return False
                counter[i] -= 1
                if counter[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        return True

"""
Dry Run 1: hand = [1, 2, 3, 6, 2, 3, 4, 7, 8], groupSize = 3
- len(hand) = 9, 9 % 3 = 0, proceed.
- counter = {1: 1, 2: 2, 3: 2, 4: 1, 6: 1, 7: 1, 8: 1}
- minHeap = [1, 2, 3, 4, 6, 7, 8], heapified -> [1, 2, 3, 4, 6, 7, 8]
- Iteration 1:
  - min_val = 1, range(1, 4):
    - i = 1: counter[1] = 1 -> 0, i == minHeap[0] (1), heappop -> minHeap = [2, 4, 3, 8, 6, 7]
    - i = 2: counter[2] = 2 -> 1
    - i = 3: counter[3] = 2 -> 1
- Iteration 2:
  - min_val = 2, range(2, 5):
    - i = 2: counter[2] = 1 -> 0, i == minHeap[0] (2), heappop -> minHeap = [3, 4, 7, 8, 6]
    - i = 3: counter[3] = 1 -> 0, i == minHeap[0] (3), heappop -> minHeap = [4, 6, 7, 8]
    - i = 4: counter[4] = 1 -> 0, i == minHeap[0] (4), heappop -> minHeap = [6, 8, 7]
- Iteration 3:
  - min_val = 6, range(6, 9):
    - i = 6: counter[6] = 1 -> 0, i == minHeap[0] (6), heappop -> minHeap = [7, 8]
    - i = 7: counter[7] = 1 -> 0, i == minHeap[0] (7), heappop -> minHeap = [8]
    - i = 8: counter[8] = 1 -> 0, i == minHeap[0] (8), heappop -> minHeap = []
- minHeap empty, return True
- Groups Formed: [1, 2, 3], [2, 3, 4], [6, 7, 8]

Dry Run 2: hand = [1, 2, 4], groupSize = 3
- len(hand) = 3, 3 % 3 = 0, proceed.
- counter = {1: 1, 2: 1, 4: 1}
- minHeap = [1, 2, 4], heapified -> [1, 2, 4]
- Iteration 1:
  - min_val = 1, range(1, 4):
    - i = 1: counter[1] = 1 -> 0, i == minHeap[0] (1), heappop -> minHeap = [2, 4]
    - i = 2: counter[2] = 1 -> 0, i == minHeap[0] (2), heappop -> minHeap = [4]
    - i = 3: 3 not in counter, return False
- Result: Correctly identifies that [1, 2, 4] cannot form a consecutive group of size 3.

Notes on the Solution:
- The min-heap approach is efficient for finding the smallest available number without repeatedly sorting.
- The check 'i != minHeap[0]' ensures numbers are used in order, preventing invalid group formations (e.g., using 2 before 1 is fully depleted).
- Edge cases like duplicates (e.g., [1, 1, 2, 2]) or gaps (e.g., [1, 3]) are handled correctly.
- Could optimize by explicitly checking counter[i] > 0 before decrementing, but current logic suffices since counter doesn’t go negative.
- This is a greedy solution: always start with the smallest number and attempt to build a group, failing fast if impossible.
"""